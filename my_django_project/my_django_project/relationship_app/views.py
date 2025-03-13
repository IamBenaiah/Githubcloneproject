from django.http import HttpResponse
from .models import Book

def book_list(request):
    books = Book.objects.all()
    book_text = "\n".join([f"{book.title} - {book.author}" for book in books])
    return HttpResponse(book_text, content_type="text/plain")

from django.shortcuts import render

def home(request):
    return render(request, 'relationship_app/home.html')
