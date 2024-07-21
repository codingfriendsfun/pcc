from django.db import models

class Blog(models.Model):
    """Model for overall blog"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model"""
        return self.text
    

class Post(models.Model):
    """Individual blog post"""
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return simple string representing post"""
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        else:
            return self.text
