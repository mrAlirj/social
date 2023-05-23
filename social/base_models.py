from django.db import models


class BaseCreatedDate(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class BaseUpdateDate(models.Model):
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
