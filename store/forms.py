from django.forms import ModelForm
from django import forms
from django.db import models
from .models import MainStore, Location, Department, Category, SubCategory

# store = MainStore.objects.all()
# loc = Location.objects.all()
# dept = Department.objects.all()
# cat = Category.objects.all()
# subcat = SubCategory.objects.all()


class AddLocation(ModelForm):
    store_name = forms.ModelChoiceField(queryset=MainStore.objects.all(), empty_label='StoreName')
    location_name = forms.CharField(max_length=25)

    class Meta:
        model = Location
        fields = '__all__'


class AddDepartment(ModelForm):
    store_name = forms.ModelChoiceField(queryset=MainStore.objects.all(), empty_label='StoreName')
    location_name = forms.ModelChoiceField(queryset=Location.objects.all(), empty_label='Location')
    department_name = forms.CharField(max_length=25)

    class Meta:
        model = Department
        fields = '__all__'


class AddCategory(ModelForm):
    store_name = forms.ModelChoiceField(queryset=MainStore.objects.all(), empty_label='StoreName')
    location_name = forms.ModelChoiceField(queryset=Location.objects.all(), empty_label='Location')
    department_name = forms.ModelChoiceField(queryset=Department.objects.all(), empty_label='Department')
    category_name = forms.CharField(max_length=25)

    class Meta:
        model = Category
        fields = '__all__'


class AddSubCategory(ModelForm):
    store_name = forms.ModelChoiceField(queryset=MainStore.objects.all(), empty_label='StoreName')
    location_name = forms.ModelChoiceField(queryset=Location.objects.all(), empty_label='Location')
    department_name = forms.ModelChoiceField(queryset=Department.objects.all(), empty_label='Department')
    category_name = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Category')
    # sub_category_name = forms.ModelChoiceField(queryset=SubCategory.objects.all(), empty_label='Sub_Category')
    sub_category_name = forms.CharField(max_length=25)

    class Meta:
        model = SubCategory
        fields = '__all__'
