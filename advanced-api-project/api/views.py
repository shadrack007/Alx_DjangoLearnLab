from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import filters
from django_filters import rest_framework

from .models import Book
from .serializers import BookSerializer

class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    # Enable filtering, searching, and ordering
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_fields = ['title', 'author', 'publication_year']
    # Enable search and ordering
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']


class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]