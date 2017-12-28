# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Student

# Create your tests here.
class StudentTestCase(TestCase):

    def test_create_student(self):
        my_student = Student.objects.create_student(
            email='fmelendezherize@gmail.com',
            password='Pikachu32.',
            names='Francisco')
        print my_student
        self.assertNotEqual(my_student, None)
