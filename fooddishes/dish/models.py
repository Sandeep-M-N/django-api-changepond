from django.db import models
from category.models import Category

# Create your models here.

def author_image_file_path(instance,filename):
    return '/'.join([str(instance.dish_name),filename])
class Dishes(models.Model):
    dish_name=models.CharField(max_length=30)
    price=models.IntegerField()
    image=models.ImageField(upload_to=author_image_file_path,null=True,blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.dish_name}'