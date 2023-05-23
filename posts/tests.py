from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken

from .models import Post


class PostAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_create_post(self):
        url = '/api/posts/'
        self.client.login(username='testuser', password='testpassword')

        data = {
            'text': 'Test post',
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['text'], 'Test post')
        self.assertEqual(response.data['user'], self.user.username)
        self.assertIsNotNone(response.data['created_date'])
        self.assertIsNotNone(response.data['last_modified'])

    def test_get_post_list(self):
        url = '/api/posts/'

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 0)

    def test_get_post_detail(self):
        post = Post.objects.create(text='Test post', user=self.user)
        url = f'/api/posts/{post.id}/'

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['text'], 'Test post')
        self.assertEqual(response.data['user'], self.user.username)
        self.assertIsNotNone(response.data['created_date'])
        self.assertIsNotNone(response.data['last_modified'])


class UserPostsAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post1 = Post.objects.create(text='First post', user=self.user)
        self.post2 = Post.objects.create(text='Second post', user=self.user)
        self.token = str(AccessToken.for_user(self.user))
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_get_user_posts(self):
        url = f'/api/posts/users/{self.user.id}/'
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

        post1_data = response.data[0]
        self.assertEqual(post1_data['text'], 'Second post')
        self.assertEqual(post1_data['likes'], 0)  # Assuming initial likes and comments are 0
        self.assertEqual(post1_data['comments'], 0)
        self.assertEqual(post1_data['user'], self.user.username)

        post2_data = response.data[1]
        self.assertEqual(post2_data['text'], 'First post')
        self.assertEqual(post2_data['likes'], 0)
        self.assertEqual(post2_data['comments'], 0)
        self.assertEqual(post2_data['user'], self.user.username)


class LikeUnlikePostAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post = Post.objects.create(text='Test post', user=self.user)
        self.token = str(AccessToken.for_user(self.user))
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_like_post(self):
        url = f'/api/posts/{self.post.id}/like/'

        # Test POST request to like the post
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, "Post liked successfully.")

        # Test GET request to retrieve liked posts
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['user'], self.user.username)
        self.assertEqual(response.data[0]['post'], self.post.id)
