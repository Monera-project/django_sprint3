from django.contrib import admin
from .models import Location, Category, Post


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'created_at')
    list_editable = ('is_published',)
    search_fields = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_published', 'created_at')
    list_editable = ('is_published',)
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'author', 'category', 'location',
        'pub_date', 'is_published'
    )
    list_editable = ('is_published',)
    search_fields = ('title', 'text')
    list_filter = ('author', 'category', 'location', 'is_published')
    date_hierarchy = 'pub_date'
