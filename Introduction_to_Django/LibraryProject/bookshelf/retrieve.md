# Retrieve and display all attributes of the books created

```python
book = Book.objects.get()

 for book in books:
    print(f'Title: {book.title}')
    print(f'Author: {book.author}')
    print(f'Publication Year: {book.publication_year}')

# Expected Output
Title: 1984
Author: George Orwell
Publication Year: 1949
```
