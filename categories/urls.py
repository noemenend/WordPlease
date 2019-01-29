from django.urls import path, include
from rest_framework.routers import DefaultRouter

from categories.api import CategoryViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet, base_name='categories')

urlpatterns = [
    # API
    path('api/1.0/', include(router.urls)),
]
