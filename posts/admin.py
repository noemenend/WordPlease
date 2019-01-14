from django.contrib import admin

from blogs.models import Blog
from categories.models import Category
from posts.models import Post

admin.site.register(Post)
admin.site.register(Blog)
admin.site.register(Category)
