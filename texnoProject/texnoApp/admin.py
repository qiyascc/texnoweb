from django.contrib import admin
from .models import CarouselImage, News, Project, Image, Startup

admin.site.register(CarouselImage)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['short_description', 'description']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'category']

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['image', 'alt_text']

admin.site.register(Startup)