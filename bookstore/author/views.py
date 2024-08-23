from django.shortcuts import render
from . models import Author
from .serializers import AuthorSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework import status
 
# Create your views here.

class AuthorViewset(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
 
    def get_serializer_class(self):
        if self.action == 'list':
            return AuthorSerializer
        return self.serializer_class
 
#get all authors
    def list(self,request):
        try:
            author_objs = Author.objects.all()
            serializer = self.get_serializer(author_objs,many=True)
            return Response({
                'status': status.HTTP_200_OK,
                'data':serializer.data
            })
 
        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status':APIException.status.code
            })