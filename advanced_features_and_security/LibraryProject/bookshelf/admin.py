from django.contrib import admin
from .models import Book
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author__name')
    list_filter = ('publication_year','author')

admin.site.register(Book)

from  .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'profile_photo', 'date_of_birth')
    
admin.site.register(CustomUser, CustomUserAdmin)