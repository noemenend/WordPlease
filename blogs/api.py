from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework_extensions.mixins import NestedViewSetMixin

from blogs.models import Blog
from blogs.permissions import BlogPermission
from blogs.serializers import BlogListSerializer, BlogSerializer
from project.utils import CaseInsensitiveOrderingFilter


class BlogsViewSet(NestedViewSetMixin, ModelViewSet):

    queryset = Blog.objects.select_related('author').all()
    permission_classes = [BlogPermission]
    filter_backends = [CaseInsensitiveOrderingFilter, SearchFilter]
    search_fields = ['author__username', 'author__first_name', 'author__last_name']
    ordering_fields = ['name']
    ordering = ['name']

    def get_serializer_class(self):
        return BlogListSerializer if self.action == 'list' else BlogSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

