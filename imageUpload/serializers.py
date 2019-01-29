from imageUpload.models import Image
from rest_framework import serializers


class ImageUploadSerializer(serializers.ModelSerializer):

    class Meta:

        model = Image
        fields = ['id', 'image', 'author']
        read_only_fields = ['author']
