from rest_framework import serializers
from category.models import Category
from .models import Dishes

class DishSerializer(serializers.ModelSerializer):
    category_id=serializers.IntegerField(write_only=True)

    class Meta:
        model=Dishes
        fields=['id','dish_name','price','image','category_id']
        read_only_fields=['id']