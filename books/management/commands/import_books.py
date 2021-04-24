import csv

from django.core.management.base import BaseCommand
from books.books_data import books
from books.models import Book


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        for book in books:
            Book.objects.create(
                name=book['title'],
                author=book['author'],
                pub_date=book['pub_date']
            )
            
