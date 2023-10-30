from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Genre, Screenshot, Movie, Director


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name", )


class MovieShotsInline(admin.TabularInline):
    model = Screenshot
    readonly_fields = ("get_image", )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110">')

    get_image.short_description = "Image"


class DirectorInline(admin.TabularInline):
    model = Director
    list_display = ("first_name", "last_name", )
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="100" height="110">')

    get_image.short_description = "Image"


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "category",)
    inlines = [MovieShotsInline, DirectorInline, ]
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="100" height="110">')

    get_image.short_description = "Poster"


admin.site.register(Director)
