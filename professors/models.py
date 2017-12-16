# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

from courses.models import Subject
from authentication.models import Profile

# Create your models here.
class ProfessorManager(models.Manager):
    '''
    Custom Professor Manager
    '''
    def create_professor(self, email, password):
        '''
        This action is made by the admin user. Create Professor with a mininum data.
        '''
        new_profile = Profile.objects.create_user(email=email, password=password)
        new_profile.user_type = 'P'
        new_profile.save()
        new_professor = Professor.objects.create(user=new_profile)
        return new_professor

    def register_professor(self, email, password, **kwargs):
        '''
        This action is made by the professor user. Complete the profile data.
        '''
        pass

    def get_professor_by_email(self, email):
        return Professor.objects.filter(user__email=email).first()

class Professor(models.Model):
    '''
    Professor Class
    '''
    names = models.CharField(max_length=200, null=True, blank=True)
    lastnames = models.CharField(max_length=200, null=True, blank=True)
    identification_number = models.CharField(max_length=20, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    skills = models.TextField(null=True, blank=True)
    subjects = models.ManyToManyField(Subject, related_name='professor_subjects')
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)

    objects = ProfessorManager()

    def __unicode__(self):
        return str(self.id)
