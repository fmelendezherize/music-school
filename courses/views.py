# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from .models import Subject, Department
from .serializers import SubjectSerializer, DepartmentSerializer
from rest_framework.response import Response

# Create your views here.
class SubjectList(APIView):
    def get(self, request, format=None):
        #instruments = Instrument.objects.select_related('department').all()
        subjects = Subject.objects.all()
        if len(subjects) > 0:
            print subjects[0].department.description
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data)

class DepartmentList(APIView):
    def get(self, request, format=None):
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)
