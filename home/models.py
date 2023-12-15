from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=16, unique= True)
    email = models.EmailField(max_length=100, unique=True)
    address = models.CharField(max_length=100)
