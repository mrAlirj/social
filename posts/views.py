from django.contrib.auth.models import User
from rest_framework import views, viewsets, status, filters, permissions
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from .models import Post, Like
from .serializers import PostSerializer, LikeSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user', 'text', 'created_date')


class UserPostsAPIView(views.APIView):
    """
    Retrieve posts for a specific user.

    Args:
        request: HTTP request object.
        user_id (int): ID of the user.

    Returns:
        Response: Serialized posts data.

    Example:
        GET /api/posts/users/<user_id>/

        Example response:
        HTTP 200 OK
        [
            {"id": 1, "text": "First post", "likes": 10, "comments": 5, "user": 1},
            {"id": 2, "text": "Second post", "likes": 5, "comments": 2, "user": 1}
        ]
    """
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        queryset = Post.objects.filter(user_id=user.id)
        serializer = PostSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class LikePostView(views.APIView):
    """
    API view to like a post and retrieve liked posts.

    Args:
        request: The HTTP request object.
        post_id (int): The ID of the post.

    Returns:
        Response: An HTTP response containing the serialized liked posts data.

    Example:
        - To like a post, make a POST request to: '/api/posts/<post_id>/like/'

        Example response for successful like:
        HTTP 201 Created

        - To retrieve liked posts, make a GET request to: '/api/posts/<post_id>/like/'

        Example response:
        HTTP 200 OK
        [
            {"id": 1, "user": 1, "post": 1},
            {"id": 2, "user": 2, "post": 1}
        ]

        - If the user has already liked the post, the response will be:
        HTTP 400 Bad Request
        "User has already liked this post."
    """
    def get(self, request, post_id):
        queryset = Like.objects.filter(post_id=post_id)
        serializer = LikeSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        user = request.user

        # Check if the user has already liked the post
        if Like.objects.filter(user=user, post=post).exists():
            return Response("User has already liked this post.", status=400)

        Like.objects.create(user=user, post=post)
        post.likes += 1
        post.save()

        return Response("Post liked successfully.", status=status.HTTP_201_CREATED)
