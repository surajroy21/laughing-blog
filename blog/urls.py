from django.urls import path

from .views import BlogListAPI, BlogDetailAPI,BlogCreateAPI,AuthorListAPI,AuthorDetailAPI,AuthorCreateAPI

app_name="blog"

urlpatterns = [
    path('list/',BlogListAPI.as_view()),
    path('detail/<int:id>/',BlogDetailAPI.as_view()),
    path('create/',BlogCreateAPI.as_view()),
    path('author/list/',AuthorListAPI.as_view()),
    path('author/detail/<int:id>/',AuthorDetailAPI.as_view()),
    path('author/create/',AuthorCreateAPI.as_view())
]