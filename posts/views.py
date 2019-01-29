from datetime import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import DetailView

from categories.models import Category
from posts.forms import PostForm
from posts.models import Post
from project.settings import ITEMS_PER_PAGE


class PostListView(View):

    def get(self, request):
        query = request.GET.get('q', '')
        qset = ()
        if query:
            qset = (
                    Q(title__icontains=query) |
                    Q(author__first_name__icontains=query) |
                    Q(author__last_name__icontains=query) |
                    Q(resume__icontains=query) |
                    Q(body__icontains=query)
            )

            last_post_published = Post.objects.select_related('author') \
                .prefetch_related('categories') \
                .filter(qset).distinct() \
                .filter(status=Post.PUBLISHED) \
                .order_by('-last_modification')
        else:
            last_post_published = Post.objects.select_related('author') \
                .prefetch_related('categories') \
                .filter(status=Post.PUBLISHED) \
                .order_by('-last_modification')

        # See all categories.
        category_list = Category.objects.all()

        #pagination
        paginator = Paginator(last_post_published, ITEMS_PER_PAGE)
        page = request.GET.get('page')
        posts = paginator.get_page(page)

        context = {
            'posts': posts,
            'categories': category_list
        }
        return render(request, 'posts/post_list.html', context)


class PostDetailView(View):

    def get(self, request, pk):

        post = get_object_or_404(Post, pk=pk)

        # See all categories.
        category_list = Category.objects.all()

        context = {
            'post': post,
            'categories': category_list
        }

        template_name = 'posts/post_detail.html'
        return render(request, template_name, context)


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
        query = request.GET.get('q', '')
        qset = ()
        if query:
            qset = (
                    Q(title__icontains=query) |
                    Q(author__first_name__icontains=query) |
                    Q(author__last_name__icontains=query) |
                    Q(resume__icontains=query) |
                    Q(body__icontains=query)
            )

            last_post_published_byCat = Post.objects.prefetch_related('categories')\
                .select_related('author') \
                .filter(qset).distinct() \
                .filter(status=Post.PUBLISHED) \
                .order_by('-last_modification').filter(categories=pk)
        else:
            last_post_published_byCat = Post.objects.prefetch_related('categories') \
                .select_related('author') \
                .filter(status=Post.PUBLISHED) \
                .order_by('-last_modification').filter(categories=pk)

        # See all categories.
        category_list = Category.objects.all()

        # pagination
        paginator = Paginator(last_post_published_byCat, ITEMS_PER_PAGE)
        page = request.GET.get('page')
        posts = paginator.get_page(page)

        context = {
            'posts': posts,
            'categories': category_list
        }
        return render(request, 'posts/post_list.html', context)