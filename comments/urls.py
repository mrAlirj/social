from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views

app_name = 'comments'

router = SimpleRouter()
router.register(r'', views.CommentViewSet, basename='comments')

urlpatterns = [
    path('posts/<int:post_id>/', views.PostCommentsAPIView.as_view(), name='post-comments'),
    path('', include(router.urls)),
]
