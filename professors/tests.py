# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.db import IntegrityError
from .models import Professor

# Create your tests here.
class ProfessorTestCase(TestCase):
    '''
    Test Case for Professor
    '''
    def test_create_professor(self):
        my_professor = Professor.objects.create_professor(
            email='fmelendezherize@gmail.com', password='Pikachu32.')
        self.assertNotEqual(my_professor, None)

    def test_create_duplicate_professor(self):
        try:
            Professor.objects.create_professor(
                email='fmelendezherize@gmail.com', password='Pikachu32.')
            Professor.objects.create_professor(
                email='fmelendezherize@gmail.com', password='Pikachu12.')
            self.fail("Not Duplicate Professors Validation Fail")
        except IntegrityError:
            pass

    def test_get_professor_email_valid(self):
        Professor.objects.create_professor(email='fmelendezherize@gmail.com', password='Pikachu32.')
        get_professor = Professor.objects.get_professor_by_email('fmelendezherize@gmail.com')
        self.assertNotEqual(get_professor, None)

    def test_get_professor_email_invalid(self):
        Professor.objects.create_professor(email='fmelendezherize@gmail.com', password='Pikachu32.')
        get_professor = Professor.objects.get_professor_by_email('wrongprofessor@gmail.com')
        self.assertEqual(get_professor, None)