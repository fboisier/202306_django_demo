from django.contrib import admin
from core.models import Author, Book, Plataforma, Movie

# Register your models here.
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Movie)
admin.site.register(Plataforma)