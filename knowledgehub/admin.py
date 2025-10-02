from django.contrib import admin
from .models import Category, Tag, Article, Book, Video, CaseStudy


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_at")
    search_fields = ("title", "author", "content")
    list_filter = ("created_at", "categories", "tags")
    filter_horizontal = ("categories", "tags")


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_date", "isbn")
    search_fields = ("title", "author", "isbn", "description")
    list_filter = ("published_date", "categories", "tags")
    filter_horizontal = ("categories", "tags")


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ("title", "url", "uploaded_at")
    search_fields = ("title", "description", "url")
    list_filter = ("uploaded_at", "categories", "tags")
    filter_horizontal = ("categories", "tags")


@admin.register(CaseStudy)
class CaseStudyAdmin(admin.ModelAdmin):
    list_display = ("title", "published_at")
    search_fields = ("title", "abstract")
    list_filter = ("published_at", "categories", "tags")
    filter_horizontal = ("categories", "tags")
