from django.db import models

class Pizza(models.Model):
    """Class to detail types of pizza"""
    name = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of model"""
        return self.text
