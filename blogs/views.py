
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.db.models.functions import Lower
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View

from blogs.forms import BlogForm
from blogs.models import Blog
from categories.models import Category
from posts.models import Post
from datetime import datetime


class BlogListView(View):

    def get(self, request):

        blog_list = Blog.objects.all().select_related('author').order_by(Lower('name'))



        return render(request, 'blogs/blog_list.html', {'blogs': blog_list, 'title': 'Blogs'})


class UserBlogsView(View):

    def get(self, request, username):

        user = get_object_or_404(User, username=username)
        blog_list = Blog.objects.filter(author=user).select_related('author').order_by(Lower('name'))

        return render(request, 'blogs/blog_list.html', {
            'blogs': blog_list,
            'title': 'Blog List - {0} {1}'.format(user.first_name, user.last_name)
        })


class BlogView(View):

    def get(self, request, pk):

        blog = get_object_or_404(Blog, id=pk)

        # See all categories.
        category_list = Category.objects.all()

        # if user is the blog propietary show all posts, otherwise show only published
        if request.user == blog.author:
            posts_list = Post.objects.select_related('author') \
                .prefetch_related('categories') \
                .filter(blog=blog.id).distinct() \
                .filter(last_modification__year__lte=datetime.now().year) \
                .order_by('-last_modification')
        else:
            posts_list = Post.objects.select_related('author') \
                .prefetch_related('categories') \
                .filter(blog=blog.id) \
                .filter(last_modification__year__lte=datetime.now().year)\
                .filter(status=Post.PUBLISHED) \
                .order_by('-last_modification')


        context = {
            'posts': posts_list,
            'categories':   category_list,
            'title': '{0}'.format(blog.name),

        }
        return render(request, 'posts/post_list.html', context)


class NewBlogView(View):

    @method_decorator(login_required)
    def get(self, request):
        form = BlogForm()
        return render(request, 'blogs/blog_new.html', {'form': form})

    @method_decorator(login_required)
    def post(self, request):
        new_blog = Blog(author=request.user)
        form = BlogForm(request.POST, instance=new_blog)

        if form.is_valid():
            new_blog = form.save()
            messages.success(request, 'Blog {0} created successfully!'.format(new_blog.name))
            form = BlogForm()

        return render(request, 'blogs/blog_new.html', {'form': form})
