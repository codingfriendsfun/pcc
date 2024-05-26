from django.db import models


class Pizza(models.Model):
    """Class to detail types of pizza"""
    name = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of pizza"""
        return self.name


class Topping(models.Model):
    """A class to detail the toppings a pizza can have"""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping = models.CharField(max_length=20)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return string representation of topping"""
        return self.topping
    