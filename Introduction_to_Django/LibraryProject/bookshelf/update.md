# Updating a Book Instance

```python
# Update the title of the book
book = Book.objects.get(id=1)
book.title = "Nineteen Eighty-Four"
book.save()

# Expected Output: book.title
'Nineteen Eighty-Four'
```
