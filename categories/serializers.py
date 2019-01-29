from rest_framework import serializers

from categories.models import Category


class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']


class CategorySerializer(CategoryListSerializer):

    class Meta(CategoryListSerializer.Meta):

        fields = '__all__'
        read_only_fields = ['id', 'pud_date', 'last_modification']
