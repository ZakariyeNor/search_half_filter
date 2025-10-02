from dal import autocomplete
from .models import Article, Book, Video, CaseStudy
from django.db.models import Q

class ArticleAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Article.objects.all()
        qs = Article.objects.all()
        
        if self.q:
            qs = qs.filter(
                Q(title__icontains=self.q) | Q(content__icontains=self.q)
            )
        return qs[:10]