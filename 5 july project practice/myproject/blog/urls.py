# blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_post/', views.create_post, name='create_post'),
    path('login/', views.login_view, name='login'), # Correctly mapped to login_view
    path('logout/', views.logout_view, name='logout'), # Add logout path
    path('register/', views.register_view, name='register'), # Correctly mapped to register_view
    # Add other paths as needed
]