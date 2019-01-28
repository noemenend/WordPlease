from django.urls import path

from blogs.views import NewBlogView, BlogListView, UserBlogsView, BlogView

urlpatterns = [
    path('blogs/', BlogListView.as_view(), name='blogs'),
    path('blogs/new/', NewBlogView.as_view(), name='blog_new'),
    path('users/<slug:username>/', UserBlogsView.as_view(), name='user-blogs'),
    path('blogs/<int:pk>/', BlogView.as_view(), name='blog'),

]