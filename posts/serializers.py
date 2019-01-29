from rest_framework import serializers

from blogs.models import Blog
from categories.serializers import CategoryListSerializer
from posts.models import Post


class PostListSerializer(serializers.ModelSerializer):

    author = serializers.SerializerMethodField()
    blog_name = serializers.SerializerMethodField()

    class Meta:

        model = Post
        fields = ['id', 'title', 'image', 'resume', 'pub_date', 'author', 'blog_name']

    def get_author(self, obj):
        return '{0} {1}'.format(obj.author.first_name, obj.author.last_name)

    def get_blog_name(self, obj):
        return obj.blog.name


class PostSerializer(PostListSerializer):

    blog = serializers.SerializerMethodField()

    class Meta(PostListSerializer.Meta):

        fields = '__all__'
        read_only_fields = ['id', 'author', 'blog']

    def validate(self, data):
        # check if blog exists and belongs to authenticated user
        try:
            blog_id = self.context.get('view').kwargs.get('parent_lookup_blogs')
            blog = Blog.objects.get(pk=blog_id)
        except:
            raise serializers.ValidationError({'detail': 'Blog not found'})
        user = self.context.get('request').user
        if blog.author == user or user.is_superuser:
            return data
        raise serializers.ValidationError({'detail': 'Blog doesn\'t belong to authenticated user'})

    def get_fields(self):
        fields = super(PostSerializer, self).get_fields()
        if self.context.get('view').action == 'retrieve':
            fields['categories'] = CategoryListSerializer(read_only=True, many=True)
        return fields

    def get_blog(self, obj):
        return {'id': obj.blog.id, 'name': obj.blog.name}
