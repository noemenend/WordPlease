from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_extensions.routers import NestedRouterMixin

from blogs.api import BlogsViewSet
from blogs.views import NewBlogView, BlogListView, UserBlogsView, BlogView
from posts.api import PostsViewSet
from users.urls import router

class NestedDefaultRouter(NestedRouterMixin, DefaultRouter):
    # Use NestedRouterMixin to have posts endpoints nested into blogs
    pass


router = NestedDefaultRouter()
blogs_router = router.register('blogs', BlogsViewSet)
blogs_router.register(
    'posts', PostsViewSet,
    base_name='blog-posts',
    parents_query_lookups=['blogs'])


urlpatterns = [
    path('blogs/', BlogListView.as_view(), name='blogs'),
    path('blogs/new/', NewBlogView.as_view(), name='blog_new'),
    path('users/<slug:username>/', UserBlogsView.as_view(), name='user-blogs'),
    path('blogs/<int:pk>/', BlogView.as_view(), name='blog'),

    #API
    path('api/1.0/', include(router.urls)),
]