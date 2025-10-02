import factory
from faker import Faker
import random
from datetime import datetime, timedelta
from knowledgehub.models import Article, Book, Video, CaseStudy, Category, Tag

fake = Faker()

# ---------------------
# Category Factory
# ---------------------
class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.LazyAttribute(lambda _: fake.word())
    slug = factory.LazyAttribute(lambda o: o.name.lower().replace(" ", "-"))

# ---------------------
# Tag Factory
# ---------------------
class TagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tag

    name = factory.LazyAttribute(lambda _: fake.word())
    slug = factory.LazyAttribute(lambda o: o.name.lower().replace(" ", "-"))

# ---------------------
# Article Factory
# ---------------------
class ArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Article

    title = factory.LazyAttribute(lambda _: fake.sentence(nb_words=6))
    author = factory.LazyAttribute(lambda _: fake.name())
    content = factory.LazyAttribute(lambda _: fake.paragraph(nb_sentences=10))
    created_at = factory.LazyAttribute(lambda _: fake.date_time_between(start_date='-5y', end_date='now'))

    @factory.post_generation
    def categories(self, create, extracted, **kwargs):
        if create:
            cats = extracted if extracted else random.sample(Category.objects.all(), k=random.randint(1,3))
            for c in cats:
                self.categories.add(c)

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if create:
            tgs = extracted if extracted else random.sample(Tag.objects.all(), k=random.randint(2,5))
            for t in tgs:
                self.tags.add(t)

# ---------------------
# Book Factory
# ---------------------
class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book

    title = factory.LazyAttribute(lambda _: fake.sentence(nb_words=5))
    author = factory.LazyAttribute(lambda _: fake.name())
    description = factory.LazyAttribute(lambda _: fake.paragraph(nb_sentences=8))
    isbn = factory.LazyAttribute(lambda _: fake.isbn13(separator="")[:20])
    published_date = factory.LazyAttribute(lambda _: fake.date_between(start_date='-20y', end_date='today'))

    @factory.post_generation
    def categories(self, create, extracted, **kwargs):
        if create:
            cats = extracted if extracted else random.sample(Category.objects.all(), k=random.randint(1,3))
            for c in cats:
                self.categories.add(c)

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if create:
            tgs = extracted if extracted else random.sample(Tag.objects.all(), k=random.randint(2,5))
            for t in tgs:
                self.tags.add(t)

# ---------------------
# Video Factory
# ---------------------
class VideoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Video

    title = factory.LazyAttribute(lambda _: fake.sentence(nb_words=5))
    url = factory.LazyAttribute(lambda _: f"https://www.youtube.com/watch?v={fake.lexify('????????')}")
    description = factory.LazyAttribute(lambda _: fake.paragraph(nb_sentences=6))
    uploaded_at = factory.LazyAttribute(lambda _: fake.date_time_between(start_date='-5y', end_date='now'))

    @factory.post_generation
    def categories(self, create, extracted, **kwargs):
        if create:
            cats = extracted if extracted else random.sample(Category.objects.all(), k=random.randint(1,3))
            for c in cats:
                self.categories.add(c)

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if create:
            tgs = extracted if extracted else random.sample(Tag.objects.all(), k=random.randint(2,5))
            for t in tgs:
                self.tags.add(t)

# ---------------------
# CaseStudy Factory
# ---------------------
class CaseStudyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CaseStudy

    title = factory.LazyAttribute(lambda _: fake.sentence(nb_words=6))
    abstract = factory.LazyAttribute(lambda _: fake.paragraph(nb_sentences=10))
    published_at = factory.LazyAttribute(lambda _: fake.date_between(start_date='-5y', end_date='today'))

    @factory.post_generation
    def categories(self, create, extracted, **kwargs):
        if create:
            cats = extracted if extracted else random.sample(Category.objects.all(), k=random.randint(1,3))
            for c in cats:
                self.categories.add(c)

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if create:
            tgs = extracted if extracted else random.sample(Tag.objects.all(), k=random.randint(2,5))
            for t in tgs:
                self.tags.add(t)
