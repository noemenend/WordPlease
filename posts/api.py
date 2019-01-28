from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import APIException
from rest_framework.filters import SearchFilter
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from blogs.models import Blog
from posts.models import Post
from posts.permissions import PostPermission, PostListPermission
from posts.serializers import PostSerializer, PostListSerializer
from project.utils import CaseInsensitiveOrderingFilter


# return 404 instead 500 if blog doesn't exist
class BlogNotFoundException(APIException):

    status_code = 404


class PostsViewSet(ModelViewSet):


    permission_classes = [PostPermission]
    filter_backends = [CaseInsensitiveOrderingFilter, SearchFilter, DjangoFilterBackend]
    search_fields = ['title', 'summary', 'body']
    ordering_fields = ['title', 'pub_date']
    ordering = ['-pub_date']
    filter_fields = ['categories']



    def get_queryset(self):
        blog_id = self.kwargs.get('parent_lookup_blogs')
        try:
            blog = Blog.objects.get(pk=blog_id)
            user = self.request.user
            if (user.is_authenticated and user == blog.author) or user.is_superuser:
                return Post.objects.filter(blog=self.kwargs.get('parent_lookup_blogs')).select_related('author').select_related('blog').prefetch_related('categories')
            return Post.objects.filter(blog=self.kwargs.get('parent_lookup_blogs'), pub_date__lte=timezone.now()).select_related('author').select_related('blog').prefetch_related('categories')
        except:
            raise BlogNotFoundException({'detail': 'Blog not found'})

    def get_serializer_class(self):
        return PostListSerializer if self.action == 'list' else PostSerializer

    def perform_create(self, serializer):
        blog = Blog.objects.get(pk=self.kwargs.get('parent_lookup_blogs'))
        serializer.save(author=blog.author, blog=blog)


class PostListViewSet(GenericViewSet, ListModelMixin):


    queryset = Post.objects.filter(pub_date__lte=timezone.now()).select_related('blog').select_related('author')
    serializer_class = PostListSerializer
    permission_classes = [PostListPermission]
    filter_backends = [CaseInsensitiveOrderingFilter, SearchFilter, DjangoFilterBackend]
    search_fields = ['title', 'summary', 'body']
    ordering_fields = ['title', 'pub_date']
    ordering = ['-pub_date']
    filter_fields = ['categories']
