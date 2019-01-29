from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class Blog(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    last_modification = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Blog, self).save(*args, **kwargs)