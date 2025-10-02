import django_filters
from django import forms
from .models import Article, Book, Video, CaseStudy, Category, Tag

# -------------------------------
# Article Filter
# -------------------------------
class ArticleFilter(django_filters.FilterSet):
    categories = django_filters.ModelChoiceFilter(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={"class": "form-select"}),
        label="Category"
    )
    tags = django_filters.ModelChoiceFilter(
        queryset=Tag.objects.all(),
        widget=forms.Select(attrs={"class": "form-select"}),
        label="Tag"
    )
    created_at__gte = django_filters.DateFilter(
        field_name="created_at", lookup_expr="gte",
        widget=forms.DateInput(attrs={"type": "date", "class": "form-control"}),
        label="From"
    )
    created_at__lte = django_filters.DateFilter(
        field_name="created_at", lookup_expr="lte",
        widget=forms.DateInput(attrs={"type": "date", "class": "form-control"}),
        label="To"
    )

    class Meta:
        model = Article
        fields = ["categories", "tags", "created_at__gte", "created_at__lte"]


# -------------------------------
# Book Filter
# -------------------------------
class BookFilter(django_filters.FilterSet):
    categories = django_filters.ModelChoiceFilter(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={"class": "form-select"}),
        label="Category"
    )
    tags = django_filters.ModelChoiceFilter(
        queryset=Tag.objects.all(),
        widget=forms.Select(attrs={"class": "form-select"}),
        label="Tag"
    )
    published_date__gte = django_filters.DateFilter(
        field_name="published_date", lookup_expr="gte",
        widget=forms.DateInput(attrs={"type": "date", "class": "form-control"}),
        label="From"
    )
    published_date__lte = django_filters.DateFilter(
        field_name="published_date", lookup_expr="lte",
        widget=forms.DateInput(attrs={"type": "date", "class": "form-control"}),
        label="To"
    )

    class Meta:
        model = Book
        fields = ["categories", "tags", "published_date__gte", "published_date__lte"]


# -------------------------------
# Video Filter
# -------------------------------
class VideoFilter(django_filters.FilterSet):
    categories = django_filters.ModelChoiceFilter(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={"class": "form-select"}),
        label="Category"
    )
    tags = django_filters.ModelChoiceFilter(
        queryset=Tag.objects.all(),
        widget=forms.Select(attrs={"class": "form-select"}),
        label="Tag"
    )
    uploaded_at__gte = django_filters.DateFilter(
        field_name="uploaded_at", lookup_expr="gte",
        widget=forms.DateInput(attrs={"type": "date", "class": "form-control"}),
        label="From"
    )
    uploaded_at__lte = django_filters.DateFilter(
        field_name="uploaded_at", lookup_expr="lte",
        widget=forms.DateInput(attrs={"type": "date", "class": "form-control"}),
        label="To"
    )

    class Meta:
        model = Video
        fields = ["categories", "tags", "uploaded_at__gte", "uploaded_at__lte"]


# -------------------------------
# Case Study Filter
# -------------------------------
class CaseStudyFilter(django_filters.FilterSet):
    categories = django_filters.ModelChoiceFilter(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={"class": "form-select"}),
        label="Category"
    )
    tags = django_filters.ModelChoiceFilter(
        queryset=Tag.objects.all(),
        widget=forms.Select(attrs={"class": "form-select"}),
        label="Tag"
    )
    published_at__gte = django_filters.DateFilter(
        field_name="published_at", lookup_expr="gte",
        widget=forms.DateInput(attrs={"type": "date", "class": "form-control"}),
        label="From"
    )
    published_at__lte = django_filters.DateFilter(
        field_name="published_at", lookup_expr="lte",
        widget=forms.DateInput(attrs={"type": "date", "class": "form-control"}),
        label="To"
    )

    class Meta:
        model = CaseStudy
        fields = ["categories", "tags", "published_at__gte", "published_at__lte"]
