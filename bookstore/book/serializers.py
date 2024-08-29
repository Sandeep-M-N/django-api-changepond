from rest_framework import serializers
from .models import BookField
from author.serializers import AuthorSerializer

class BookSerializer(serializers.ModelSerializer):
    author_id = serializers.IntegerField(write_only = True)

    class Meta:
        model = BookField
        fields = ['id','title','rating','author_id']
        read_only_fields=['id']