# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from models import Professor
import courses

# Create your tests here.
class ProfessorTestCase(TestCase):

    def test_create_professor(self):
        my_professor = Professor.create_professor(email='fmelendezherize@gmail.com', password='Pikachu32.')
        self.assertNotEqual(my_professor, None)

    def test_create_duplicate_professor(self):
        my_professor = Professor.create_professor(email='fmelendezherize@gmail.com', password='Pikachu32.')
        print my_professor

        my_professor = Professor.create_professor(email='fmelendezherize@gmail.com', password='Pikachu12.')
        print my_professor
