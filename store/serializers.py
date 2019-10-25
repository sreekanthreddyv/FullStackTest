from rest_framework import serializers
from .models import MainStore, Location, Department, Category, SubCategory


class MainStoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = MainStore
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    main = MainStoreSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Location
        fields = '__all__'


class DeptSerializer(serializers.ModelSerializer):
    locations = LocationSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Department
        fields = '__all__'
        # fields = ('store_name', 'location_nam', 'department_name')  # , 'category_name',
        # fields = ('category_name', 'sub_category_name')


class CategorySerializer(serializers.ModelSerializer):
    locations = DeptSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Category
        fields = '__all__'


class SubCatSerializer(serializers.ModelSerializer):
    locations = CategorySerializer(many=True, read_only=True, required=False)

    class Meta:
        model = SubCategory
        fields = '__all__'
