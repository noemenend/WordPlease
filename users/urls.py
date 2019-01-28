from django.urls import path

from users.views import LoginView, LogoutView, SignUpView, UsersListView



urlpatterns = [
path('login', LoginView.as_view(), name='login'),
path('logout', LogoutView.as_view(), name='logout'),
path('signup', SignUpView.as_view(), name='signup'),
path('users', UsersListView.as_view(), name='users')
    ]
