import rest_framework

from .models import Book
from .serializers import BookSerializer

# Create your views here.
class BookListView(rest_framework.generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer