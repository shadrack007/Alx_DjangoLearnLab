from django.contrib import admin
from  .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'profile_photo', 'date_of_birth')

    
    
admin.site.register(CustomUser, CustomUserAdmin)
