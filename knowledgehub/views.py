from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Article, Book, Video, CaseStudy, Category, Tag

from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank

# -----------------------------
# Home / Dashboard View
# -----------------------------
def home(request):
    # Get latest items from each resource
    articles = Article.objects.all().order_by('-created_at')[:5]
    books = Book.objects.all().order_by('-published_date')[:5]
    videos = Video.objects.all().order_by('-uploaded_at')[:5]
    case_studies = CaseStudy.objects.all().order_by('-published_at')[:5]
    
    context = {
        'articles': articles,
        'books': books,
        'videos':videos,
        'case_studies': case_studies,
    }
    
    return render(
        request,
        'knowledgehub/home.html',
        context
    )

# -----------------------------
# Generic Detail View
# -----------------------------
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'knowledgehub/article_detail.html', {'article': article})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'knowledgehub/book_detail.html', {'book': book})

def video_detail(request, pk):
    video = get_object_or_404(Video, pk=pk)
    return render(request, 'knowledgehub/video_detail.html', {'video': video})

def case_study_detail(request, pk):
    case_study = get_object_or_404(CaseStudy, pk=pk)
    return render(request, 'knowledgehub/case_study_detail.html', {'case_study': case_study})

# -----------------------------
# Search View (All Resources)
# search() view uses icontains
# -----------------------------
""" def search(request):
    query = request.GET.get('q', '')
    results_articles = Article.objects.none()
    results_books = Book.objects.none()
    results_videos = Video.objects.none()
    results_case_studies = CaseStudy.objects.none()

    if query:
        # Simple icontains search
        results_articles = Article.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
        results_books = Book.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query) | Q(author__icontains=query)
        )
        results_videos = Video.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
        results_case_studies = CaseStudy.objects.filter(
            Q(title__icontains=query) | Q(abstract__icontains=query)
        )

    context = {
        'query': query,
        'results_articles': results_articles,
        'results_books': results_books,
        'results_videos': results_videos,
        'results_case_studies': results_case_studies,
    }
    return render(request, 'knowledgehub/search.html', context) """


# -----------------------------
# Search View (All Resources) 
# with Full-Text Search
# -----------------------------
def search(request):
    query = request.GET.get('q', '')
    results_articles = Article.objects.none()
    results_books = Book.objects.none()
    results_videos = Video.objects.none()
    results_case_studies = CaseStudy.objects.none()

    if query:
        search_query = SearchQuery(query)
        
        # Articles
        results_articles = Article.objects.annotate(
            search=SearchVector("title", "content")
        ).filter(search=search_query).annotate(
            rank=SearchRank(SearchVector("title", "content"), search_query)
            ).order_by("-rank")
        
        # Books
        results_books = Book.objects.annotate(
            search=SearchVector("title", "description", "author")
        ).filter(search=search_query).annotate(
            rank=SearchRank(SearchVector("title", "description", "author"), search_query)
        ).order_by("-rank")
        
        # Videos
        results_videos = Video.objects.annotate(
            search=SearchVector("title", "description")
        ).filter(search=search_query).annotate(
            rank=SearchRank(SearchVector("title", "description"), search_query)
        ).order_by("-rank")
        
        # Case Studies
        results_case_studies = CaseStudy.objects.annotate(
            search=SearchVector("title", "abstract")
        ).filter(search=search_query).annotate(
            rank=SearchRank(SearchVector("title", "abstract"), search_query)
        ).order_by("-rank")

    context = {
        'query': query,
        'results_articles': results_articles,
        'results_books': results_books,
        'results_videos': results_videos,
        'results_case_studies': results_case_studies,
    }
    return render(request, 'knowledgehub/search.html', context)

        
    