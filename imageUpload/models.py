from django.contrib.auth.models import User
from django.db import models


class Image(models.Model):

    image = models.ImageField(upload_to='')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
