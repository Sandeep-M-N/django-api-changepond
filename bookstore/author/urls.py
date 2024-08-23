from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewset
 
router = DefaultRouter()
router.register('', AuthorViewset, basename='author')
app_name ='author'
 
urlpatterns=[
    path('', include(router.urls))
]