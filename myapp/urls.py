

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.PostListV3.as_view()),
    path('<int:pk>/delete/', views.deletePost),
    path('<int:pk>/', views.PostDetailV3.as_view()),
]
