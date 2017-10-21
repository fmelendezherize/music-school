# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from courses.models import Subject

# Create your models here.
class Professor(models.Model):
    names = models.CharField(max_length=200)
    lastnames = models.CharField(max_length=200)
    identification_number = models.CharField(max_length=20, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    skills = models.TextField(null=True, blank=True)
    subjects = models.ManyToManyField(Subject, related_name='professor_subjects')    

    def __unicode__(self):
        return self.names + " " + str(self.lastnames)
