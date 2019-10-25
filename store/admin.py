from django.contrib import admin
from .models import MainStore, Location, Department, Category, SubCategory

# Register your models here.
admin.site.register(MainStore)
admin.site.register(Location)
admin.site.register(Department)
admin.site.register(Category)
admin.site.register(SubCategory)

