from django.db import models


# Pizza and toppings.

class Pizza(models.Model):
    """Class representing pizza."""

    text = models.TextField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string."""

        return self.text
