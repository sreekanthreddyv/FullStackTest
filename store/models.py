from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User
from django.db.models.signals import post_delete
from django.dispatch import receiver
import json
import ast


# Create your models here.
class MainStore(models.Model):
    store_name = models.CharField(max_length=80)  # , default='BanjaraHills')

    def __str__(self):
        return self.store_name


class Location(models.Model):
    # user = models.ForeignKey(User)
    store_name = models.ForeignKey(MainStore, on_delete=models.CASCADE, null=True)
    # parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True, on_delete=models.CASCADE)
    # store_name = models.ManyToOneRel(MainStore, field_name='store_name', on_delete=models.CASCADE)
    location_name = models.CharField(max_length=30, unique=True, default='Center')

    def __str__(self):
        return self.location_name


class Department(models.Model):
    store_name = models.ForeignKey(MainStore, on_delete=models.CASCADE, null=True)
    location_name = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    # parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True, on_delete=models.CASCADE)
    department_name = models.CharField(max_length=50, default='Bakery')

    def __str__(self):
        return self.department_name


class Category(models.Model):
    store_name = models.ForeignKey(MainStore, on_delete=models.CASCADE, null=True)
    location_name = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    department_name = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    # parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name


class SubCategory(models.Model):
    store_name = models.ForeignKey(MainStore, on_delete=models.CASCADE, null=True)
    location_name = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    department_name = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    # parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True, on_delete=models.CASCADE)
    sub_category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.sub_category_name


class Model2(models.Model):
    store_name = models.ForeignKey(MainStore, on_delete=models.CASCADE)
    location_name = models.CharField(max_length=50)
    # parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True, on_delete=models.CASCADE)
    department_name = models.CharField(max_length=50)
    category_name = models.CharField(max_length=50)
    sub_category_name = models.CharField(max_length=50)