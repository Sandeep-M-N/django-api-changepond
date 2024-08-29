from django.db import models
from author.models import Author
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.
class BookField(models.Model):
    title=models.CharField(max_length=20)
    rating=models.IntegerField(
        validators=[MinValueValidator(1),MaxValueValidator(10)]
        )
    author=models.ForeignKey(Author,on_delete=models.CASCADE)

    def __str__(self):
        return self.title