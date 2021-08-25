from django.contrib import admin
from .models import *

# Register your models here.

# admin.site.register(books)
admin.site.register(User)

@admin.register(book)
class admin(admin.ModelAdmin):
    list_display = ['id','title', 'author', 'isbn','date_of_publication']



