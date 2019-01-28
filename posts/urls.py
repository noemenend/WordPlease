from django.urls import path, include
from rest_framework.routers import DefaultRouter

from posts.api import PostListViewSet
from posts.views import PostDetailView, NewPostView, PostListView, PostListByCategoryView

router = DefaultRouter()
router.register('posts', PostListViewSet, base_name='posts')

urlpatterns = [


    path('posts/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('posts/new_post', NewPostView.as_view(), name='new_post'),
    path('', PostListView.as_view(), name='home'),
    path('postsbyCat/<int:pk>', PostListByCategoryView.as_view(), name='categoriesPost'),

    # API
    path('api/1.0/', include(router.urls)),
]