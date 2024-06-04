from django.db import models


# Pizza and toppings.

class Pizza(models.Model):
    """Class representing pizza."""

    name = models.TextField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string."""

        return self.name


class Topping(models.Model):
    """Class representing toppings."""

    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name_plural = 'toppings'

    def __str__(self):
        """Topping attributes."""

        if len(str(self.name)) >= 50:

            return f"{self.name[:50]}..."

        else:
            return self.name

