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
    places = model.IntegerField(default=25)
    students_registered = models.ManyToManyField(Student, related_name='courses')
    students_enrolled = models.ManyToManyField(Student, related_name='courses')

    def register_student(student):
        #Insert a pending student and decrease places
        #Validar que el studiante este en otro cursos
        pass
    
    def enroll_student(student):
        #Approve a student
        pass

    def reject_student(student):
        #Remove student and increace places
        pass

    def __unicode__(self):
        return self.name
    