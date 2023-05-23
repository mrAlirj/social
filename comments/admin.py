from django.contrib import admin
from django.contrib.humanize.templatetags.humanize import naturaltime

from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_date', 'last_modified')
    list_filter = ('user', 'post', 'created_date')
    list_per_page = 20
    search_fields = ('user_username', 'post', 'created_date', 'text')

    @admin.display(description='created_date')
    def created_date(self, obj):
        return naturaltime(obj.created_date)

    @admin.display(description='last_modified')
    def created_date(self, obj):
        return naturaltime(obj.last_modified)
