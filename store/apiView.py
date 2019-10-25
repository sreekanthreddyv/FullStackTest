from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import MainStore, Location, Department, SubCategory
from .serializers import DeptSerializer, SubCatSerializer


class DeptList(APIView):
    def get(self, request):
        depts = Department.objects.all()
        data = DeptSerializer(depts, many=True).data
        return Response(data)


class DeptDetail(APIView):
    def get(self, request, pk):
        depts = get_object_or_404(Department, pk=pk)
        data = DeptSerializer(depts).data
        return Response(data)


class SubCatList(APIView):
    def get(self, request):
        subcats = SubCategory.objects.all()
        data = SubCatSerializer(subcats, many=True).data
        return Response(data)


class SubCatDetail(APIView):
    def get(self, request, pk):
        subcats = get_object_or_404(SubCategory, pk=pk)
        data = SubCatSerializer(subcats).data
        return Response(data)
