# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Course
from students.models import Student

# Create your tests here.
class CoursesTestCase(TestCase):

    def test_create_course(self):
        my_student = Student.objects.create_student(
            email='fmelendezherize@gmail.com',
            password='Pikachu32.',
            names='Francisco')
        print Student.objects.all()
        self.assertNotEqual(my_student, None)
        my_courses = Course.objects.create(name='curso de guitarra')
        print Course.objects.all()
        