# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from courses.models import Subject
from authentication.models import Profile, ProfileManager

# Create your models here.
class Professor(models.Model):
    identification_number = models.CharField(max_length=20, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    skills = models.TextField(null=True, blank=True)
    subjects = models.ManyToManyField(Subject, related_name='professor_subjects')
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)

    def __unicode__(self):
        return self.names + " " + str(self.lastnames)

    @staticmethod
    def create_professor(email, password):
        '''
        This action is made by the admin user. Create Professor with a mininum data.
        '''
        user = Profile.objects.create_user(email=email, password=password)
        user.user_type = 'P'
        user.save()
    
    def register_professor(email, password, **kwargs):
        '''
        This action is made by the professor user. Complete the profile data.
        '''

        pass
    
