from django.db import models
from django.urls import reverse

# Create your models here.
# Add the Comics class & list and view function below the imports
class Comic(models.Model):
    name = models.CharField(max_length=50)
    published = models.IntegerField()
    author = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    worth = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
      return reverse('detail', kwargs={'comic_id': self.id})