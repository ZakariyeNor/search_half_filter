import factory
from faker import Faker
from knowledgehub.models import Article, Book, Video, CaseStudy, Category, Tag

fake = Faker()

# ---------------------
# Category Factory
# ---------------------
class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.LazyAttribute(lambda _: fake.word())


# ---------------------
# Tag Factory
# ---------------------
class TagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tag

    name = factory.LazyAttribute(lambda _: fake.word())


# ---------------------
# Article Factory
# ---------------------
class ArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Article

    title = factory.LazyAttribute(lambda _: fake.sentence())
    author = factory.LazyAttribute(lambda _: fake.name())
    content = factory.LazyAttribute(lambda _: fake.text())

    @factory.post_generation
    def categories(self, create, extracted, **kwargs):
        if create and extracted:
            for category in extracted:
                self.categories.add(category)

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if create and extracted:
            for tag in extracted:
                self.tags.add(tag)


# ---------------------
# Book Factory
# ---------------------
class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book

    title = factory.LazyAttribute(lambda _: fake.sentence())
    author = factory.LazyAttribute(lambda _: fake.name())
    description = factory.LazyAttribute(lambda _: fake.text())

    @factory.post_generation
    def categories(self, create, extracted, **kwargs):
        if create and extracted:
            for category in extracted:
                self.categories.add(category)

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if create and extracted:
            for tag in extracted:
                self.tags.add(tag)


# ---------------------
# Video Factory
# ---------------------
class VideoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Video

    title = factory.LazyAttribute(lambda _: fake.sentence())
    url = factory.LazyAttribute(lambda _: fake.url())
    description = factory.LazyAttribute(lambda _: fake.text())

    @factory.post_generation
    def categories(self, create, extracted, **kwargs):
        if create and extracted:
            for category in extracted:
                self.categories.add(category)

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if create and extracted:
            for tag in extracted:
                self.tags.add(tag)


# ---------------------
# CaseStudy Factory
# ---------------------
class CaseStudyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CaseStudy

    title = factory.LazyAttribute(lambda _: fake.sentence())
    abstract = factory.LazyAttribute(lambda _: fake.text())

    @factory.post_generation
    def categories(self, create, extracted, **kwargs):
        if create and extracted:
            for category in extracted:
                self.categories.add(category)

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if create and extracted:
            for tag in extracted:
                self.tags.add(tag)
