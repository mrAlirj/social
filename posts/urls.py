from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views

app_name = 'posts'

router = SimpleRouter()
router.register(r'', views.PostViewSet, basename='posts')

urlpatterns = [
    path('<int:post_id>/like/', views.LikePostView.as_view(), name='like-post'),
    path('users/<int:user_id>/', views.UserPostsAPIView.as_view(), name='user-posts'),
    path('', include(router.urls)),
]
