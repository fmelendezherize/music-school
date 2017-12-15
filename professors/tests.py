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
