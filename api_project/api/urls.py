from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import BookList
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book_all')

urlpatterns = [
    path('', include(router.urls)),  # Include the router URLs
    path('books/', BookList.as_view(), name='book-list'),
]