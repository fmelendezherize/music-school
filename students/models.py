# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import date
from authentication.models import Profile

class StudentManager(models.Manager):
    def create_student(self, email, password, **kwargs):
        user = Profile.objects.create_user(email=email, password=password)
        user.user_type = 'S'
        user.save()
        #create student
        student = Student()
        student.user = user
        student.names = kwargs['names']
        student.save()
        return student

# Create your models here.
class Student(models.Model):
    '''
    Student Class
    '''
    names = models.CharField(max_length=200)
    lastnames = models.CharField(max_length=200)
    identification_number = models.CharField(max_length=20)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    date_birth = models.DateField(default=date.today)
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)

    objects = StudentManager()

    def __unicode__(self):
        return self.names + " " + str(self.lastnames)
