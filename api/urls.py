from django.urls import path

from api import views

urlpatterns = [
    path('', views.home, name='home'),
    path("blog-list/", views.blog_list, name="blog-list"),
    path("blog-details/<str:pk>", views.blog_details, name="blog-details"),
    path("blog-create/", views.blog_create, name="blog-create"),
    path("blog-update/<str:pk>", views.blog_update, name="blog-update"),
    path("blog-delete/<str:pk>", views.blog_delete, name="blog-delete"),
]