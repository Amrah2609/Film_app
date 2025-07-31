from django.contrib import admin
from django.utils.html import format_html
from core.models import TeamPage, Movie, Video, Genre, Contact, ContactSettings, BlogPost, Tag, SocialMedia, ContactInfo

class GenreTabularInline(admin.TabularInline):
    model = Genre.movie.through
    extra = 2

class VideoTabularInlineAdmin(admin.TabularInline):
    model = Video
    extra = 1

@admin.register(TeamPage)
class TeamPageAdmin(admin.ModelAdmin):
    list_display = ('name', 'title')
    search_fields = ('name', 'title')
    list_filter = ('title',)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'year', 'slug', 'image_preview', 'created_date', 'get_imdb_rating_as_stars', 'get_streamvibe_rating_as_stars']
    search_fields = ('name', 'description', 'year',)
    list_filter = (
        'is_background', 'is_carousel', 'is_upcoming', 'is_series',
        'is_trend', 'is_featured', 'is_trailer', 'is_popular'
    )
    readonly_fields = ('slug', 'image_preview')
    inlines = [VideoTabularInlineAdmin, GenreTabularInline]

    # Metodları burada düzgün indentasiya edin
    def get_imdb_rating_as_stars(self, obj):
        return self.render_stars(obj.imdb_rating)

    def get_streamvibe_rating_as_stars(self, obj):
        return self.render_stars(obj.streamvibe_rating)

    def render_stars(self, rating):
        # Əgər rating None-dursa, 0 təyin et
        if rating is None:
            rating = 0

        full_stars = int(rating)
        half_star = 1 if rating - full_stars >= 0.5 else 0
        empty_stars = 5 - full_stars - half_star
        stars = (
                '<i class="fa-solid fa-star"></i>' * full_stars +
                '<i class="fa-solid fa-star-half-stroke"></i>' * half_star +
                '<i class="fa-regular fa-star"></i>' * empty_stars
        )
        return format_html(stars)

    def image_preview(self, obj):
        if obj.background_image:
            return format_html('<img src="{}" width="100" />', obj.background_image.url)
        return '-'

    image_preview.short_description = 'Image Preview'  # Admin panelində başlıq
    get_imdb_rating_as_stars.short_description = 'IMDb Rating'
    get_streamvibe_rating_as_stars.short_description = 'Streamvibe Rating'


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Contact)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'message')

@admin.register(ContactSettings)
class ContactSettingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'phone')
    fieldsets = (
        ("İletişim Bilgileri", {
            'fields': ('phone', 'email', 'address'),
        }),
        ("Harita ve SVG", {
            'fields': ('map_iframe', 'contact_icon_svg'),
        }),
        ("Öne Çıkan Film", {
            'fields': ('featured_movie',),
        }),
    )

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ("title", "author", "published_at")
    search_fields = ('title', 'content')
    filter_horizontal = ('tags', )

    def display_tags(self, obj):
        return ", ".join(tag.name for tag in obj.tags.all())

    display_tags.short_description = 'Tags'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ("name", "url", "icon_class")

admin.site.register(ContactInfo)
