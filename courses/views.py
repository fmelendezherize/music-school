# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from .models import Instrument, Department
from .serializers import InstrumentSerializer, DepartmentSerializer
from rest_framework.response import Response

# Create your views here.
class InstrumentList(APIView):
    def get(self, request, format=None):
        #instruments = Instrument.objects.select_related('department').all()
        instruments = Instrument.objects.all()
        print instruments[0].department.description
        serializer = InstrumentSerializer(instruments, many=True)
        return Response(serializer.data)

class DepartmentList(APIView):
    def get(self, request, format=None):
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)
