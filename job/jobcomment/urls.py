from django.contrib import admin
from django.urls import path
from . import views

urlpatterns =[
    path('<int:blog_id>', views.detail, name='detail'),
    path('newblog/', views.blogpost, name="newblog")
]