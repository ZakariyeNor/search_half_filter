from django.core.management.base import BaseCommand
from knowledgehub.factories import (
    CategoryFactory, TagFactory,
    ArticleFactory, BookFactory,
    VideoFactory, CaseStudyFactory
)
import random

class Command(BaseCommand):
    help = "Seed KnowledgeHub data"

    def handle(self, *args, **options):
        # ---------------------
        # Create Categories (10–15)
        # ---------------------
        category_names = [
            "Programming", "Artificial Intelligence", "Data Science", "Law",
            "History", "Philosophy", "Design", "Marketing", "Business",
            "Health", "Psychology"
        ]
        categories = []
        for name in category_names:
            categories.append(CategoryFactory(name=name))

        # ---------------------
        # Create Tags (30–50)
        # ---------------------
        tag_names = [
            "Python", "Django", "React", "Machine Learning", "NLP",
            "Civil Law", "Criminal Law", "UX", "Branding", "Startups",
            "Mental Health", "Cognitive Science", "SQL", "AI Ethics",
            "Data Analysis", "Frontend", "Backend", "Deep Learning",
            "TensorFlow", "PyTorch", "Business Strategy", "Marketing 101",
            "Design Thinking", "Healthcare", "Philosophy of Mind", "History of AI"
        ]
        tags = []
        for name in tag_names:
            tags.append(TagFactory(name=name))

        self.stdout.write(self.style.SUCCESS(f"Created {len(categories)} categories and {len(tags)} tags"))

        # ---------------------
        # Create Articles (500–1000)
        # ---------------------
        for _ in range(500):
            ArticleFactory(categories=categories, tags=tags)

        # ---------------------
        # Create Books (200–500)
        # ---------------------
        for _ in range(300):
            BookFactory(categories=categories, tags=tags)

        # ---------------------
        # Create Videos (300–500)
        # ---------------------
        for _ in range(400):
            VideoFactory(categories=categories, tags=tags)

        # ---------------------
        # Create Case Studies (100–200)
        # ---------------------
        for _ in range(150):
            CaseStudyFactory(categories=categories, tags=tags)

        self.stdout.write(self.style.SUCCESS(
            "Seeded Articles, Books, Videos, and Case Studies successfully!"
        ))
