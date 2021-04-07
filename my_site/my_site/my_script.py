# exec(open('myscript.py').read())
# from django.db.models import Count, Sum, F
# from django.db.models import ExpressionWrapper, DecimalField
from p_library.models import Author, Publisher, Book

#target_book = Book.objects.exclude(author__country = "RU")
# target_book = Book.objects.filter(copy_count__gte = 2)
# target_book = Book.objects.filter(author__full_name = "Douglas Adams")
# target_book = Book.objects.filter(author__book__gt = 1)
# price_target_book = target_book.aggregate(Sum('price') * Sum('copy_count'))
# print("test")
publishers = Publisher.objects.get(id=1)
print(publishers.book_set.all())
# count_target_book = target_book.aggregate(Sum('copy_count'))
# for auth in Author.objects.all():
    # if auth.book_set.count() > 1:
    #     total_cost = auth.book('price') * auth.book('copy_count')
   	    # print(auth.full.name, total_cost)
# print(auth.full_name, auth.id, auth.book_set.count())
# for book in Book.objects.filter(auth.id):
#     total_cost = book.price * book.copy_count
# print('Author: {} - Number of Books
# : {}'.format(a.full_name, a.book_set.count()))
# # no_horsman_pushkin_books = Book.objects.all().filter(author=pushkin).exclude(title__icontains="всадник")\
# for Book.author in Book.objects.all():
# 	print(Author('full_name'))
# target_books = Book.objects.all().filter('title' > 1)
# print(target_books.exists())
