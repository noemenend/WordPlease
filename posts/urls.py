from django.urls import path

from posts.views import PostDetailView, NewPostView, PostListView, PostListByCategoryView

urlpatterns = [


    path('posts/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('posts/new_post', NewPostView.as_view(), name='new_post'),
    path('', PostListView.as_view(), name='home'),
    path('postsbyCat/<int:pk>', PostListByCategoryView.as_view(), name='categoriesPost')
]