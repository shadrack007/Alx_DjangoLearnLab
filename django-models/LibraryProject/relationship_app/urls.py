from django.urls import path
from .views import list_books, LibraryDetailsView   

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailsView.as_view(), name='library_details'),
]