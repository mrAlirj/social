from rest_framework import viewsets, filters, views, status, permissions
from rest_framework.response import Response

from .models import Comment
from .serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user', 'post', 'text', 'created_date')


class PostCommentsAPIView(views.APIView):
    """
    Retrieve comments for a specific post.

    Args:
        request: HTTP request object.
        post_id (int): ID of the post.

    Returns:
        Response: Serialized comments data.

    Example:
        GET /api/comments/posts/<post_id>/

        Example response:
        [
            {"id": 1, "text": "This is a comment.", "user": 1, "post": 1},
            {"id": 2, "text": "Another comment.", "user": 2, "post": 1}
        ]
    """
    def get(self, request, post_id):
        queryset = Comment.objects.filter(post_id=post_id)
        serializer = CommentSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
