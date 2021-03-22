from django.urls import path

from .views import LoginView, UserListView, LogoutView, UserCreateView, ResetPasswordView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('list_users/', UserListView.as_view(), name='list-users'),
    path('add-user/', UserCreateView.as_view(), name='add-user'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('reset_password/<int:pk>/', ResetPasswordView.as_view(), name='reset-password'),


]