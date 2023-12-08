from django.db import models


class Item(models.Model):
    """
    Represents item object
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
