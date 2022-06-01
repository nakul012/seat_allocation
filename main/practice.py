from unittest.util import _MAX_LENGTH
from django.contrib.auth import User
from django.contrib.auth import AbstractUser

from django.db import models


class User(AbstractUser,                                                                                                          models.Model):
    username = models.CharField(max_length=40)
    first_name = models.CharField(max_length=40)
    email = models.EmailField(blank=True,null=True)
    last_name = models.CharField(max_length=40,blank=True,null=True)

class Organisation(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)


class Department(models.Model):
    name = models.CharField(max_length=40)
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)

class Employee(models.Model):
    name = models.ForeignKey(User,on_delete=models.PROTECT)
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)


class Project(models.Model):
    name = models.CharField(max_length=40)
    Employee = models.ManyToManyField(Employee,on_delete=models.CASCADE)
    employee_roll = models.CharField(max_length=100)



