from django.db import models
from django.db.models.fields.files import ImageField

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/pics')
    disc = models.TextField()

