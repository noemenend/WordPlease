from django.urls import path, include
from rest_framework.routers import DefaultRouter

from blogs.api import BlogsViewSet
from blogs.views import NewBlogView, BlogListView, UserBlogsView, BlogView
from users.urls import router

router = DefaultRouter()
blogs_router = router.register('blogs', BlogsViewSet)

urlpatterns = [
    path('blogs/', BlogListView.as_view(), name='blogs'),
    path('blogs/new/', NewBlogView.as_view(), name='blog_new'),
    path('users/<slug:username>/', UserBlogsView.as_view(), name='user-blogs'),
    path('blogs/<int:pk>/', BlogView.as_view(), name='blog'),

    #API
    path('api/1.0/', include(router.urls)),
]