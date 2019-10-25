from django.db import models

# Create your models here.
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User
from django.db.models.signals import post_delete
from django.dispatch import receiver
import json
import ast


# Create your models here.
class MainStore(models.Model):
    store_name = models.CharField(max_length=80, default='BanjaraHills')

    def __str__(self):
        return self.store_name


class Location(models.Model):
    # user = models.ForeignKey(User)
    store_name = models.ForeignKey(MainStore, on_delete=models.CASCADE)
    location_name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.location_name


class Department(MPTTModel, models.Model):
    location_name = models.ManyToOneRel(Location, on_delete=models.CASCADE)
    department_name = models.CharField(max_length=50)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True, on_delete=models.CASCADE, )

    def __str__(self):
        return self.department_name


class Category(MPTTModel, models.Model):
    location_name = models.OneToOneField(Location, on_delete=models.CASCADE)
    department_name = models.ForeignKey(Department, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=50)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True, on_delete=models.CASCADE, )

    def __str__(self):
        return self.category_name


class SubCategory(MPTTModel):
    location_name = models.ManyToOneRel(Location, on_delete=models.CASCADE)
    department_name = models.ManyToOneRel(Department, on_delete=models.CASCADE)#, default='Dairy')
    category_name = models.ManyToOneRel(Category, on_delete=models.CASCADE)
    sub_category_name = models.CharField(max_length=50)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True, on_delete=models.CASCADE, )

    def __str__(self):
        return self.sub_category_name
