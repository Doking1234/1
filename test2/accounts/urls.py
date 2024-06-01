# accounts/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register, edit_profile, profile, UserLoginView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('profile/', profile, name='profile'),
    path('edit-profile/', edit_profile, name='edit_profile'),
]
