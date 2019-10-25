from django.urls import path
# from .models import Location, Department, Category, SubCategory
from store import views, apiview
from django.conf.urls import url

urlpatterns = [
    path('deplist/', views.DepartmentList.as_view()),
    path("depts/", apiview.DeptList.as_view(), name="depts_list"),
    path("depts/<int:pk>/", apiview.DeptDetail.as_view(), name="depts_detail"),
    path("subcats/", apiview.SubCatList.as_view(), name="subcats_list"),
    path("subcats/<int:pk>/", apiview.SubCatDetail.as_view(), name="subcats_detail"),
    path("hello/", views.hacker)
]