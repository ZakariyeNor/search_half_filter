from django.urls import path
from . import views
from .autocomplete import ArticleAutocomplete

app_name = "knowledgehub"

urlpatterns = [
    # Home page
    path('', views.home, name='home'),

    # Article detail
    path('article/<int:pk>/', views.article_detail, name='article_detail'),

    # Book detail
    path('book/<int:pk>/', views.book_detail, name='book_detail'),

    # Video detail
    path('video/<int:pk>/', views.video_detail, name='video_detail'),

    # Case study detail
    path('case-study/<int:pk>/', views.case_study_detail, name='case_study_detail'),

    # Search view
    path('search/', views.search, name='search'),
    
    # Autocomplete
    path('autocomplete/articles/', ArticleAutocomplete.as_view(), name='article-autocomplete'),
]
