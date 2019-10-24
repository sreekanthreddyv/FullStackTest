from django.contrib.auth import logout
from django.shortcuts import render
from rest_framework import generics
from .models import Location, Department, Category, SubCategory
from .serializers import StoreSerializer


# Create your views here.
class SubCategoryList(generics.ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = StoreSerializer
    # logout()
