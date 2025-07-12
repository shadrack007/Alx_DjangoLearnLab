# Deleting a Book Instance

```python
book = Book.objects.get(id=1)
book.delete()

# Expected Output
(1, {'bookshelf.Book': 1})
```
