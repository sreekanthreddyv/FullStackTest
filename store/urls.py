from django.urls import path
from .models import Location, Department, Category, SubCategory
from store import views

urlpatterns = [
    path('subcats/', views.SubCategoryList.as_view()),
]