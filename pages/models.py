from django.db import models
from django.urls import reverse


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    author = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])
