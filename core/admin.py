from django.contrib import admin

from core.models import TeamPage, Movie, Video, Genre, Contact, ContactSettings, BlogPost,  Tag, SocialMedia, ContactInfo



class GenreTabularInline(admin.TabularInline):
    model = Genre.movie.through
    extra = 2

class VideoTabularInlineAdmin(admin.TabularInline):
    model = Video
    extra = 1



@admin.register(TeamPage)
class TeamPageAdmin(admin.ModelAdmin):
    list_display = ('name','title')
    search_fields = ('name','title')
    list_filter = ('title',)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name',  'year', 'slug', 'image_preview', 'created_date' ]
    search_fields = ('name', 'description', 'year',)
    list_filter = (
        'is_background','is_carousel','is_upcoming', 'is_series',
        'is_trend','is_featured', 'is_trailer','is_popular')
    readonly_fields = ('slug', 'image_preview')
    inlines = [VideoTabularInlineAdmin, GenreTabularInline, ]


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
