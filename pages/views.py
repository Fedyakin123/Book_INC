from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    )
from django.urls import reverse_lazy
from .models import Book
# Create your views here.


class BookListView(ListView):
    model = Book
    template_name ='home.html'
    context_object_name = 'all_books'

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'

class BookUpdateView(UpdateView):
    model = Book
    template_name = 'book_update.html'
    fields = ['title', 'year', 'author', 'price']

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_delete.html'
    success_url = reverse_lazy('home')

class BookCreateView(CreateView):
    model = Book
    template_name = 'book_create.html'
    fields = ['title', 'year', 'author', 'price']
