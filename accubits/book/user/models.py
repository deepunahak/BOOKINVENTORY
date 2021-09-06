from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(null=True, max_length=127)
    email = models.EmailField(null=True, max_length=127, unique=True)
    password = models.CharField(null=True, max_length=127)
