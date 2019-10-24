from rest_framework import serializers
from .models import Location, Department, Category, SubCategory


class StoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubCategory
        # fields = ('location_name', 'department_name', 'category_name',
        fields = ('category_name', 'sub_category_name')
