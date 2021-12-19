from django.db import models

# Create your models here.

class Message(models.Model):
    name = models.CharField(max_length=200, default='')
    email = models.EmailField(max_length=254)
    message = models.TextField(max_length=300)