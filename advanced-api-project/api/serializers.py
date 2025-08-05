from rest_framework import serializers

from .models import Book, Author

# Serializer for Book model
class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['id','title','published_year']

    # validate that the published year is not in the future
    def validate_published_year(self, value):

        from datetime import datetime
        # get the current year
        current_year = datetime.now().year
        
        if value > current_year:
            raise serializers.ValidationError("Published year cannot be in the future.")
        return value

# Serializer for Author model
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']

