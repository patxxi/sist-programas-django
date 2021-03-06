from django.db import models

# Create your models here.

class Category(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    name = models.CharField(max_length=120)

    def __str__(self):
        return f'{self.id}:{self.name}'


class Products(models.Model):
    """Contains all relevant information about products"""

    id_product = models.CharField(max_length=20 ,unique=True, primary_key=True)
    name = models.CharField(max_length=120)

    category = models.ForeignKey('Category',
                                 on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.CharField(max_length=120)

    def __str__(self):
        return f" {self.name} by {self.brand}, category: {self.category} price: ${self.price} "
