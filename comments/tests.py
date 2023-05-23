from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken

from posts.models import Post

from .models import Comment


class CommentAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post = Post.objects.create(text='Test post', user=self.user)
        self.token = str(AccessToken.for_user(self.user))
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_create_comment(self):
        url = '/api/comments/'

        data = {
            'text': 'Test comment',
            'post': self.post.id,
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['text'], 'Test comment')
        self.assertEqual(response.data['user'], self.user.username)
        self.assertEqual(response.data['post'], self.post.id)
        self.assertIsNotNone(response.data['created_date'])

    def test_get_comment_list(self):
        url = '/api/comments/'

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 0)

    def test_get_comment_detail(self):
        comment = Comment.objects.create(text='Test comment', user=self.user, post=self.post)
        url = f'/api/comments/{comment.id}/'

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['text'], 'Test comment')
        self.assertEqual(response.data['user'], self.user.username)
        self.assertEqual(response.data['post'], self.post.id)
        self.assertIsNotNone(response.data['created_date'])


class PostCommentsAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post = Post.objects.create(text='Test post', user=self.user)
        self.token = str(AccessToken.for_user(self.user))
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_get_post_comments(self):
        url = f'/api/comments/posts/{self.post.id}/'

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_get_post_comments_with_existing_comments(self):
        Comment.objects.create(text='Test comment 1', user=self.user, post=self.post)
        Comment.objects.create(text='Test comment 2', user=self.user, post=self.post)
        url = f'/api/comments/posts/{self.post.id}/'

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['text'], 'Test comment 1')
        self.assertEqual(response.data[0]['user'], self.user.username)
        self.assertEqual(response.data[0]['post'], self.post.id)
        self.assertIsNotNone(response.data[0]['created_date'])
        self.assertEqual(response.data[1]['text'], 'Test comment 2')
        self.assertEqual(response.data[1]['user'], self.user.username)
        self.assertEqual(response.data[1]['post'], self.post.id)
        self.assertIsNotNone(response.data[1]['created_date'])
