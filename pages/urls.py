from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookUpdateView,
    BookDeleteView,
    BookCreateView,
)

urlpatterns = [
    path('', BookListView.as_view(), name='home'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('book/<int:pk>/update', BookUpdateView.as_view(), name='book_update'),
    path('book/<int:pk>/delete', BookDeleteView.as_view(), name='book_delete'),
    path('book/new/', BookCreateView.as_view(), name="book_create"),
]