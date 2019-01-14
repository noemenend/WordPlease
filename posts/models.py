from django.db import models

from blogs.models import Blog
from categories.models import Category


class Post(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    resume = models.TextField()
    body = models.TextField()
    image = models.FileField()
    creation_date = models.DateTimeField(auto_now_add=True)
    pub_date = models.DateTimeField()
    last_modification = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title
