from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=150)
    resume = models.CharField(max_length=250)
    body = models.TextField()
    image = models.FileField()
    creation_date = models.DateTimeField(auto_now_add=True)
    pub_date = models.DateTimeField()
    last_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
