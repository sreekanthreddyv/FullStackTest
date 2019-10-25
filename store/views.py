from django.contrib.auth import logout
from django.shortcuts import render
from rest_framework import generics
from .models import Location, Department, Category, SubCategory
from .serializers import DeptSerializer


# Create your views here.
class DepartmentList(generics.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DeptSerializer


def hacker(request):
    data = SubCategory.objects.all()
    context = {'data': data}
    return render(request, 'hacker.html', context)

