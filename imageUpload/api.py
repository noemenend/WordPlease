from rest_framework import viewsets

from imageUpload.models import Image
from imageUpload.permission import ImageUploadPermission
from imageUpload.serializers import ImageUploadSerializer


class ImageUploadViewSet(viewsets.ModelViewSet):

    permission_classes = [ImageUploadPermission]
    queryset = Image.objects.select_related('author').all()
    serializer_class = ImageUploadSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
