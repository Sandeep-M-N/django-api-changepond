from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DishViewset
 
router = DefaultRouter()
router.register('', DishViewset, basename='dish')
app_name ='dish'
 
urlpatterns=[
    path('', include(router.urls))
]
