from django.contrib.auth import logout
from django.shortcuts import render
from rest_framework import generics
from .models import Location, Department, Category, SubCategory
from .serializers import DeptSerializer
from .forms import AddCategory, AddLocation, AddDepartment, AddSubCategory


# Create your views here.
class DepartmentList(generics.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DeptSerializer


def hacker(request):
    data = SubCategory.objects.all()
    context = {'data': data}
    return render(request, 'hacker.html', context)


def add_location_details(request):
    if request.method == 'POST':
        form = AddLocation(request.POST)
        if form.is_valid():
            u = form.save()
            details = Location.objects.all()
            return render(request, 'location_upload.html', {'details': details})
    else:
        form_class = AddLocation
    return render(request, 'hello.html', {'form': form_class})


def add_department_details(request):
    if request.method == 'POST':
        form = AddDepartment(request.POST)
        if form.is_valid():
            u = form.save()
            details = Department.objects.all()
            return render(request, 'department_upload.html', {'details': details})
    else:
        form_class = AddDepartment
    return render(request, 'hello.html', {'form': form_class})


def add_category_details(request):
    if request.method == 'POST':
        form = AddCategory(request.POST)
        if form.is_valid():
            u = form.save()
            details = Category.objects.all()
            return render(request, 'category_upload.html', {'details': details})
    else:
        form_class = AddCategory
    return render(request, 'hello.html', {'form': form_class})


def add_subcategory_details(request):
    if request.method == 'POST':
        form = AddSubCategory(request.POST)
        if form.is_valid():
            u = form.save()
            details = SubCategory.objects.all()
            return render(request, 'sub_category_upload.html', {'details': details})
    else:
        form_class = AddSubCategory
    return render(request, 'hello.html', {'form': form_class})
