from django.shortcuts import render
from.models import Dishes
from .serializers import DishSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework import status,parsers
from rest_framework.decorators import action
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
 
# Create your views here.
class DishViewset(ModelViewSet):
    queryset = Dishes.objects.all()
    serializer_class = DishSerializer
    parser_classes = (parsers.FormParser,parsers.MultiPartParser,parsers.FileUploadParser)
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]


    def get_serializer_class(self):
        if self.action == 'list':
            return DishSerializer
        elif self.action=='create':
             return DishSerializer
        elif self.action == 'upload_image':
            return DishSerializer
        return self.serializer_class
    # @action(methods=['POST'],detail=True,url_path='upload-image')
    # def upload_image(self,request,pk=None):
    #     dish_objs =self.get_object()
    #     serializer=self.get_serializer(dish_objs,data=request.data)
    #     if not serializer.is_valid():
    #         return Response({
    #                 'status': status.HTTP_400_BAD_REQUEST,
    #                 'data':serializer.errors,
    #                 'message':'Inavlid Data'
    #             })
    #     serializer.save()
    #     return Response({
    #                 'status': status.HTTP_200_OK,
    #                 'data':serializer.data,
    #                 'message': 'dish Image uploaded Successfully'
    #             })
 
#get all dishes
    def list(self,request):
        try:
            dish_objs = Dishes.objects.all()
            serializer = self.get_serializer(dish_objs,many=True)
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
# create an dish 
    def create(self,request):
        try:
            serializer = self.get_serializer(data=request.data)
            if not serializer.is_valid():
                return Response({
                    'status': status.HTTP_400_BAD_REQUEST,
                    'data':serializer.errors,
                    'message':'Inavlid Data'
                })
            serializer.save()
            return Response({
                'status': status.HTTP_201_CREATED,
                'data': serializer.data,
                'message': 'Dish created successfully'
            })
 
        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status':APIException.status.code
            })
        
# get single dish

    def retrive(self,request,pk=None):
        try:
            id = pk
            if id is not None:
                dish_objs = self.get_object()
                serializer = self.get_serializer(dish_objs)
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
#update all fields of dish
    def update(self,request,pk=None):
        try:
            dish_objs = self.get_object()
            serializer = self.get_serializer(dish_objs,data=request.data,partial=False)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({
                    'status': status.HTTP_400_BAD_REQUEST,
                    'data':serializer.errors,
                    'message':'Inavlid Data'
                })
            serializer.save()
            return Response({
                    'status': status.HTTP_200_OK,
                    'data':serializer.data,
                    'message': 'Dishes Updated Successfully'
                })
 
        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status':APIException.status.code
            })
    #update specifie
    def partial_update(self,request,pk=None):
        try:
            dish_objs = self.get_object()
            serializer = self.get_serializer(dish_objs,data=request.data,partial=True)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({
                    'status': status.HTTP_400_BAD_REQUEST,
                    'data':serializer.errors,
                    'message':'Inavlid Data'
                })
            serializer.save()
            return Response({
                    'status': status.HTTP_200_OK,
                    'data':serializer.data,
                    'message': 'Dish Partial Updated Successfully'
                })
 
        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status':APIException.status.code
            })
 
    def destroy(self,request,pk):
        try:
            id=pk
            dish_objs = self.get_object()
            dish_objs.delete()
 
            return Response({
                'status': status.HTTP_200_OK,
                'message':'Dish deleted successfully'
            })
 
        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status':APIException.status.code
            })
        