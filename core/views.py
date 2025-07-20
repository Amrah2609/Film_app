from itertools import count

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from core.forms import ContactForm
from core.models import TeamPage, Movie, Video, ContactSettings, Contact, BlogPost, Tag, SocialMedia
from django.db.models import Count

# Create your views here.


def index(request):
    context = {
    "carousel_movie": Movie.objects.filter(is_carousel=True),
    "trend_movie": Movie.objects.filter(is_trend=True),
    "background_movie": Movie.objects.filter(is_background=True),
    "series_background": Movie.objects.filter(is_series_background=True).first(),
    "film_background": Movie.objects.filter(is_film_background=True).first(),
    "upcoming_movie": Movie.objects.filter(is_upcoming=True),
    "series_movie": Movie.objects.filter(is_series=True),
    "top_rated_movie": Movie.objects.filter(is_top_rated=True),
    "film_rated_movie": Movie.objects.filter(is_film_rated_movie=True),
    "social_media": SocialMedia.objects.all(),}
    return render(request, "index.html", context)


def team(request):
    content = {"team": TeamPage.objects.all()}
    return render(request, "team.html", content)


def movie(request):
    context = {
    "trend_movie": Movie.objects.filter(is_trend=True),
    "featured_movie": Movie.objects.filter(is_featured=True),
    "trailer_movie": Movie.objects.filter(is_trailer=True),
    "popular_movie": Movie.objects.filter(is_popular=True),}
    return render(request, "movie.html", context)


def movie_detail(request, slug):
    movie = get_object_or_404(Movie, slug=slug)
    return render(request, "movie-details.html", {"movie": movie})


def web_series(request):
    context = {"series_movie": Movie.objects.filter(is_series=True),
               "web_background": Movie.objects.filter(is_web_background=True).first(),
               "rated_scenes": Movie.objects.filter(is_rated_scenes=True),
               "most_watch_series": Movie.objects.filter(is_most_watch_series=True),
               "rated_series": Movie.objects.filter(is_rated_series=True),}
    return render(request, "web-series.html", context)




def contact_page(request):
    contact_movie = Movie.objects.first()
    settings = ContactSettings.objects.first()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for contacting us.")
            return redirect("contact")
        else:
            print(form.errors)
            messages.error(request, "Something went wrong.")
    else:
        form = ContactForm()
    return render(request, "contact.html", {
        "contact_form": form,
        "contact_movie": contact_movie,
        "settings": settings,
    })


def blog_page(request):
    posts = BlogPost.objects.order_by('-published_at')
    recent_posts = BlogPost.objects.order_by('-published_at')[:5]
    tags = Tag.objects.all()

    q = request.GET.get('q')
    tag_slug = request.GET.get('tag')

    if q:
        posts = posts.filter(title__icontains=q)

    if tag_slug:
        posts = posts.filter(tags__slug=tag_slug)

    return render(request, "news.html", {
        "posts": posts,
        "recent_posts": recent_posts,
        "tags": tags,
    })



def blog_details(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    recent_posts = BlogPost.objects.exclude(slug=slug).order_by('-published_at')[:5]
    tags = Tag.objects.all()
    return render(request, "news-details.html", {
        "post": post,
        "recent_posts": recent_posts,
        "tags": tags
    })


def error_page(request):
    return render(request, "404.html")


def search(request):
    query = request.GET.get("q")
    movies = Movie.objects.filter(name__icontains=query)
    return render(request, "search.html", {"movies": movies})