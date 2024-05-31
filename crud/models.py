from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)

class Product(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()