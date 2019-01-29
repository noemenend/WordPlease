from django.urls import path, include
from rest_framework.routers import DefaultRouter

from imageUpload.api import ImageUploadViewSet

router = DefaultRouter()
router.register('image_upload', ImageUploadViewSet, base_name='image_uploads')


urlpatterns = [

    # API
    path('api/1.0/', include(router.urls)),
]