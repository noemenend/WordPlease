from datetime import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import DetailView

from categories.models import Category
from posts.forms import PostForm
from posts.models import Post


class PostListView(View):

    def get(self, request):
        last_post_published = Post.objects.select_related('author') \
            .prefetch_related('categories')\
            .filter(status=Post.PUBLISHED) \
            .order_by('-last_modification')

        # See all categories.
        category_list = Category.objects.all()

        context = {
            'posts': last_post_published,
            'categories': category_list
        }
        return render(request, 'posts/post_list.html', context)


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'


class NewPostView(View):

    @method_decorator(login_required)
    def get(self, request):
        form = PostForm(user=request.user)
        return render(request, 'posts/new_post.html', {'form': form})

    @method_decorator(login_required)
    def post(self, request):
        new_post = Post(author=request.user)
        form = PostForm(request.POST, request.FILES, instance=new_post, user=request.user)
        if form.is_valid():
            new_post = form.save()
            messages.success(request, 'Post {0} created successfully!'.format(new_post.title))
            form = PostForm(user=request.user)
        return render(request, 'posts/new_post.html', {'form': form})


class PostListByCategoryView(View):

    def get(self, request, pk):
        last_post_published_byCat = Post.objects.prefetch_related('categories')\
            .select_related('author') \
            .filter(status=Post.PUBLISHED) \
            .order_by('-last_modification').filter(categories=pk)

        # See all categories.
        category_list = Category.objects.all()

        context = {
            'posts': last_post_published_byCat,
            'categories': category_list
        }
        return render(request, 'posts/post_list.html', context)
