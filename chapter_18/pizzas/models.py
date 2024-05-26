from django.db import models


class Pizza(models.Model):
    """A pizza"""
    name = models.CharField(max_length=50)
    # Debated adding date_added, but do we really care? 
    # No

    def __str__(self):
        """Return a string representation of the model"""
        return self.text
