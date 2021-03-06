from django.db import models

# Create your models here.


# określa kategorie w sklepie

class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

# określa rozmiar w sklepie

class Size(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


# określa towar w sklepie

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    current_quantity = models.IntegerField()
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name='products')
    category = models.ManyToManyField(Category, related_name='products')


