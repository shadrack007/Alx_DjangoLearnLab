
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User

from  .models import Book, Author

class BookAPITest(APITestCase):
    def setUp(self):
         # Create a test user
        self.user = User.objects.create_user(username='testuser', password='pass123')    
        self.author = Author.objects.create(name="Test Author")
        self.book = Book.objects.create(title="Test Book", author=self.author, publication_year=2021)
    
    def test_list_books(self):
        url = reverse('book_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], self.book.title)
        self.assertEqual(response.data[0]['publication_year'], self.book.publication_year)

    def test_create_book(self):
        self.client.login(username='testuser', password='pass123')
        url = reverse('book_create')
        data = {
            'title': 'New Book',
            'author': self.author,
            'publication_year': 2022
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_detail_book(self):
        url = reverse('book_detail', kwargs={'pk': self.book.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)

    def test_update_book(self):
        self.client.login(username='testuser', password='pass123')
        url = reverse('book_update', kwargs={'pk': self.book.pk})
        data = {
            'title': 'Updated Book',
            'author': self.author.id,
            'publication_year': 2023
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book')

    def test_delete_book(self):
        self.client.login(username='testuser', password='pass123')
        url = reverse('book_delete', kwargs={'pk': self.book.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(pk=self.book.pk).exists())


    def test_filter_books(self):
        url = reverse('book_list') + '?title=Test Book'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Book')

    def test_search_books(self):
        url = reverse('book_list') + '?search=Test Author'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    

    def test_order_books(self):
        url = reverse('book_list') + '?ordering=publication_year'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 2021)
