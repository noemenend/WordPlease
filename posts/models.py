from django.contrib.auth.models import User
from django.db import models

from blogs.models import Blog
from categories.models import Category


class Post(models.Model):

    PUBLISHED = 'PUB'
    NO_PUBLISHED = 'NPUB'

    STATUS = (
        (PUBLISHED, 'Published'),
        (NO_PUBLISHED, 'No Published')
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    resume = models.TextField()
    body = models.TextField()
    image = models.FileField()
    creation_date = models.DateTimeField(auto_now_add=True)
    pub_date = models.DateTimeField()
    last_modification = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category)
    status = models.CharField(max_length=4, choices=STATUS)

    def __str__(self):
        return '{0} ({1})'.format(self.title, self.get_status_display())
