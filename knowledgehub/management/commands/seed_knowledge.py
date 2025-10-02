from django.core.management.base import BaseCommand
from knowledgehub.factories import (
    CategoryFactory, TagFactory,
    ArticleFactory, BookFactory,
    VideoFactory, CaseStudyFactory
)

class Command(BaseCommand):
    help = "Seed KnowledgeHub data"

    def handle(self, *args, **options):
        # ---------------------
        # Create Categories and Tags
        # ---------------------
        categories = CategoryFactory.create_batch(5)
        tags = TagFactory.create_batch(10)

        self.stdout.write(self.style.SUCCESS(f"Created {len(categories)} categories and {len(tags)} tags"))

        # ---------------------
        # Create resources
        # ---------------------
        ArticleFactory.create_batch(5, categories=categories, tags=tags)
        BookFactory.create_batch(5, categories=categories, tags=tags)
        VideoFactory.create_batch(5, categories=categories, tags=tags)
        CaseStudyFactory.create_batch(5, categories=categories, tags=tags)

        self.stdout.write(self.style.SUCCESS("Seeded 5 Articles, 5 Books, 5 Videos, 5 CaseStudies"))
