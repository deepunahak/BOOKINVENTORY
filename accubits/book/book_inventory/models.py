from django.db import models


# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    count = models.IntegerField()


class BookBorrow(models.Model):
    book_id = models.IntegerField()
    user_id = models.IntegerField()
    date = models.DateField()

