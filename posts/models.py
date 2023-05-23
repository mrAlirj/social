from django.db import models
from django.contrib.auth.models import User

from social.base_models import BaseCreatedDate, BaseUpdateDate


class Post(BaseCreatedDate, BaseUpdateDate):
    text = models.TextField()
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.created_date} - {self.id}"

    class Meta:
        ordering = ['-created_date']


class Like(BaseCreatedDate):
    user = models.ForeignKey(User, related_name='post_likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='all_likes', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_date']
