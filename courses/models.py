# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from students.models import Student

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __unicode__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    department = models.ForeignKey(Department, related_name='subject_deparment', on_delete=models.CASCADE)

    def __unicode__(self):
        return str(self.id) + ":" + self.name

class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    students = models.ManyToManyField(Student, related_name='courses')

    def __unicode__(self):
        return self.name
    