from django.contrib import admin
from .models import Post, Like


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'likes', 'comments', 'created_date', 'last_modified')
    list_filter = ('user', 'created_date')
    list_per_page = 20
    search_fields = ('user_username', 'text', 'created_date')


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_date')
    list_filter = ('user', 'created_date')
    list_per_page = 20
    search_fields = ('user_username', 'post_text', 'created_date')
