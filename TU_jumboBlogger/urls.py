"""TU_jumboBlogger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from jumboBlogger import views
from django.contrib.auth import views as auth_views
from django.urls import path
from jumboBlogger.views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostListView.as_view(), name='blog-home'),  # url for homepage
    path('register/', views.register, name='register'),  # url for registration
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # url for logging in
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),  # url for user's posts
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # url for showing details of a post
    path('post/new/', PostCreateView.as_view(), name='post-create'),  # url for creating new post
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  # url for updating a given post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  # url for deleting a post
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),  # url for log out
]
urlpatterns += staticfiles_urlpatterns()