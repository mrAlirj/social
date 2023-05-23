from django.db import models
from django.contrib.auth.models import User

from social.base_models import BaseCreatedDate, BaseUpdateDate
from posts.models import Post


class Comment(BaseCreatedDate, BaseUpdateDate):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')

    def __str__(self):
        return f"{self.user} - {self.created_date} - {self.post.id}"

    class Meta:
        ordering = ['created_date']
