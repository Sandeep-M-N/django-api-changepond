from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    age=models.IntegerField()
