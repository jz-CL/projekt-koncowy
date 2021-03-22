from django.db import models

# Create your models here.


# określa kategorie w sklepie

class Category(models.Model):
    name = models.CharField(max_length=64)
    kod = models.CharField(max_length=5)

    def __str__(self):
        return self.name

# określa rozmiar w sklepie

class Size(models.Model):
    name = models.CharField(max_length=64)
    kod = models.CharField(max_length=5)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=64)
    kod = models.CharField(max_length=5)

    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=64)
    kod = models.CharField(max_length=5)

    def __str__(self):
        return self.name


# określa towar w sklepie
#  nazwa/numer katalogowa/y - identyfikacja po rozmiarze
#  nazwa produktu może się dublować nr katalogowy jest unikalny

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    # identyfikator
    identifier_exists = models.CharField(max_length=32)
    current_quantity = models.IntegerField()
    # size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name='products')
    size = models.ManyToManyField(Size, related_name='products')
    color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name='products')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products')
    category = models.ManyToManyField(Category, related_name='products')

    def __str__(self):
        return self.name
        # return self.name + ' - ' + str(self.size.name)

class Koszyk(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='koszyks')
    ile = models.IntegerField()