from django.urls import path
from .views import (
    index,
    team,
    movie,
    movie_detail,
    contact_page,
    blog_page,
    blog_details,
    web_series,
    error_page,
    search,
)


urlpatterns = [
    path("", index, name="index"),
    path("team/", team, name="team"),
    path("movie/", movie, name="movie"),
    path("movie/<str:slug>", movie_detail, name="movie_detail"),
    path("contact/", contact_page, name="contact"),
    path('blog/', blog_page, name='blog_page'),
    path('blog/<slug:slug>/', blog_details, name='blog_details'),
    path("web_series/", web_series, name="web_series"),
    path("error/", error_page, name="error_page"),
    path("search/", search, name="search"),
]
