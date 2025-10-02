from django.db import models
from django.utils.text import slugify

from django.contrib.postgres.indexes import GinIndex, BTreeIndex
from django.contrib.postgres.search import SearchVectorField

# Category model (e.g. Programming, AI, Law, History)
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    
    class Meta:
        verbose_name_plural = "Categories"
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    
    def __str__(self):
        return self.name

# Tag model (keywords for articles/books/videos/etc.)
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name


# Article resource
class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, related_name="articles")
    tags = models.ManyToManyField(Tag, related_name="articles", blank=True)

    search_vector = SearchVectorField(null=True)

    class Meta:
        indexes = [
            GinIndex(fields=['search_vector'], name="article_search_vector_idx"),
            GinIndex(name="article_title_content_trgm_idx",
                     opclasses=["gin_trgm_ops", "gin_trgm_ops"],
                     fields=["title", "content"]),
        ]
               
    def __str__(self):
        return self.title


# Book resource
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    published_date = models.DateField(blank=True, null=True)
    isbn = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(blank=True)
    categories = models.ManyToManyField(Category, related_name="books")
    tags = models.ManyToManyField(Tag, related_name="books", blank=True)
    
    search_vector = SearchVectorField(null=True)

    class Meta:
        indexes = [
            GinIndex(fields=['search_vector'], name="book_sv_idx"),
            GinIndex(
                fields=['title', 'author', 'description'],
                opclasses=["gin_trgm_ops", "gin_trgm_ops", "gin_trgm_ops"],
                name="book_trgm_idx"
            )
        ]
        
    def __str__(self):
        return f"{self.title} by {self.author}"


# Video resource
class Video(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    description = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, related_name="videos")
    tags = models.ManyToManyField(Tag, related_name="videos", blank=True)

    search_vector = SearchVectorField(null=True)

    class Meta:
        indexes = [
           GinIndex(fields=['search_vector'], name="vid_sv_idx"),
            GinIndex(fields=['title', 'description'], opclasses=["gin_trgm_ops", "gin_trgm_ops"], name="vid_trgm_idx"),
        ]
         
    def __str__(self):
        return self.title
    

# Case Study resource
class CaseStudy(models.Model):
    title = models.CharField(max_length=255)
    abstract = models.TextField()
    published_at = models.DateField(blank=True, null=True)
    categories = models.ManyToManyField(Category, related_name="case_studies")
    tags = models.ManyToManyField(Tag, related_name="case_studies", blank=True)
    
    search_vector = SearchVectorField(null=True)

    class Meta:
        indexes = [
            GinIndex(fields=['search_vector'], name="cs_sv_idx"),
            GinIndex(fields=['title', 'abstract'], opclasses=["gin_trgm_ops", "gin_trgm_ops"], name="cs_trgm_idx"),
        ]
        
    def __str__(self):
        return self.title
