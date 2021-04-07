from django.contrib import admin

from p_library.models import Author, Book, Publisher


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Publisher)
class AuthorAdmin(admin.ModelAdmin):
    pass
