from django.contrib import admin
from django.urls import path, register_converter
from books.views import books_view, other_books
from .converters import DateConverter

register_converter(DateConverter, 'date')

urlpatterns = [
    # path('', books_view, name='books'),
    path('admin/', admin.site.urls),
    path('books/', books_view, name='books'),
    path('books/<date:pub_date>/', books_view, name='books_filter'),
    path('books/<date:pub_date>/<option>/', other_books, name='books_filter_href'),
]
