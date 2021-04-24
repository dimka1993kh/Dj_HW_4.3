from django.shortcuts import render
from books.models import Book
from django.core.paginator import Paginator

def books_view(request, pub_date=None):
    template = 'books/books_list.html'
    books = Book.objects.all()
    next_true = False
    prev_true = False
    if pub_date:
        books = Book.objects.filter(pub_date=pub_date)
        next_true = Book.objects.filter(pub_date__gt=pub_date)
        prev_true = Book.objects.filter(pub_date__lt=pub_date)
    context = {
        'books' : books,
        'pub_date' : pub_date,
        'prev' : 'prev',
        'next' : 'next',
        'next_true' : next_true, 
        'prev_true' : prev_true
    }
    
    return render(request, template, context)

def other_books(request, pub_date, option):
    template = 'books/books_other.html'
    print('option',option)
    if option == 'next':
        books = Book.objects.filter(pub_date__gt=pub_date)
    elif option == 'prev':
        books = Book.objects.filter(pub_date__lt=pub_date)
    context = {
        'books' : books,
        'pub_date' : pub_date
    }
    return render(request, template, context)
