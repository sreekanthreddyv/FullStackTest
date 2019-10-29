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
    path("hello/", views.hacker),
    path("add_location/", views.add_location_details),
    path("add_department/", views.add_department_details),
    path("add_category/", views.add_category_details),
    path("add_sub_category/", views.add_subcategory_details),
    path("display/", views.add_location_details),
    path("display/", views.add_department_details),
    path("display/", views.add_category_details),
    path("display/", views.add_subcategory_details),
]