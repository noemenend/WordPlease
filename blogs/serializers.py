from django.utils.text import slugify
from rest_framework import serializers

from blogs.models import Blog
from posts.models import Post


class UserSerializer(serializers.Serializer):

    id = serializers.ReadOnlyField()
    username = serializers.CharField()


class BlogListSerializer(serializers.HyperlinkedModelSerializer):

    author = UserSerializer()

    post_count = serializers.SerializerMethodField()
    url = serializers.HyperlinkedIdentityField(view_name='blog-detail', format='html')

    class Meta:

        model = Blog
        fields = ['id', 'url', 'name', 'author', 'post_count']
        read_only_fields = ['author', 'slug']

    def get_post_count(self, obj):
        return Post.objects.select_related('blogs').prefetch_related('categories').filter(blog=obj).count()


class BlogSerializer(BlogListSerializer):

    class Meta(BlogListSerializer.Meta):

        fields = ['id', 'name', 'description', 'author']

    def get_fields(self):
        fields = super(BlogSerializer, self).get_fields()
        view = self.context.get('view')
        if view.action in ['update', 'create', 'partial_update']:
            fields.get('author').read_only = True
        return fields

    def validate_name(self, value):
        slug = slugify(value)
        # validacion si estoy actualizando un blog
        if self.instance is not None and self.instance.slug != slug and Blog.objects.filter(slug=slug).exists():
            raise serializers.ValidationError("Blog '{0}' already exists".format(value))

        # validacion si estoy creando un blog
        if self.instance is None and Blog.objects.filter(slug=slug).exists():
            raise serializers.ValidationError("Blog '{0}' already exists".format(value))

        return value
