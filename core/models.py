from django.db import models
from django.utils.text import slugify
from django.utils.html import mark_safe
from django.utils.timezone import now
from packaging.tags import Tag


# Create your models here.


class Movie(models.Model):
    background_image = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=250)
    year = models.IntegerField()
    description = models.TextField()
    duration = models.DurationField(null=True, blank=True)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    is_background = models.BooleanField(default=False)
    is_carousel = models.BooleanField(default=False)
    is_upcoming = models.BooleanField(default=False)
    is_series = models.BooleanField(default=False)
    is_trend = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    is_trailer = models.BooleanField(default=False)
    is_popular = models.BooleanField(default=False)

    is_series_background = models.BooleanField(default=False)
    is_web_background = models.BooleanField(default=False)
    is_film_background = models.BooleanField(default=False)
    is_top_rated = models.BooleanField(default=False)
    is_rated_scenes = models.BooleanField(default=False)
    is_film_rated_movie = models.BooleanField(default=False)
    is_most_watch_series = models.BooleanField(default=False)
    is_rated_series = models.BooleanField(default=False)


    def __str__(self):
        return self.name


    def image_preview(self):
        return mark_safe(f"<img width='200' src='{self.background_image.url}' alt='{self.id}' />")

    def save(self, *args, **kwargs):
        if not self.slug:
            time = now()
            timestamp = int(time.timestamp())  # Noktasız integer zaman
            self.slug = f"{slugify(self.name)}-{timestamp}"
        super(Movie, self).save(*args, **kwargs)


    def get_genres(self):
        genres= self.genres.all()
        result = []
        if genres:
            for genre in genres:
                result.append(genre.name)
            return " / ".join(result)
        else:
            return []


    def video_link(self):
        video = self.videos.all().first()
        if video:
            return video.url
        else:
            return None


    def formatted_duration(self):
        total_minutes = int(self.duration.total_seconds() // 60)
        hours, minutes = divmod(total_minutes, 60)
        return f"{hours}h {minutes}m"


class Video(models.Model):
    url = models.URLField(null=True, blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='videos')

    def __str__(self):
        return self.url


class Genre(models.Model):
    name = models.CharField(max_length=250)
    movie = models.ManyToManyField(Movie, related_name='genres')

    def __str__(self):
        return self.name



class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    message = models.TextField()

    class Meta:
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"

    def __str__(self):
        return self.name


class ContactSettings(models.Model):
    featured_movie = models.ForeignKey(Movie, null=True, blank=True, on_delete=models.SET_NULL)
    map_iframe = models.TextField("Google Map Embed Code", blank=True)
    contact_icon_svg = models.TextField("Contact Icon SVG", blank=True)

    phone = models.CharField("Phone Number", max_length=50, blank=True)
    email = models.EmailField("Contact Email", blank=True)
    address = models.CharField("Address", max_length=255, blank=True)

    def __str__(self):
        return "Contact Page Settings"



class TeamPage(models.Model):
    name = models.CharField(max_length=250)
    title = models.CharField(max_length=100)
    image = models.ImageField()
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name





class   Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=100, default='Admin')
    published_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True)
    excerpt = models.TextField(max_length=500, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/', null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_tags(self):
        return ", ".join(tag.name for tag in self.tags.all())

    def __str__(self):
        return self.title


class SocialMedia(models.Model):
    PLATFORM_CHOICES = [
        ('facebook', 'Facebook'),
    ('twitter', 'Twitter'),
    ('instagram', 'Instagram'),
    ('linkedin', 'LinkedIn'),]

    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    url = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.platform.capitalize()