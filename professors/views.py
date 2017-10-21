# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from .models import Professor
from .serializers import ProfessorSerializer
from rest_framework.response import Response

# Create your views here.
class ProfessorList(APIView):
    def get(self, request, format=None):
        professors = Professor.objects.all()
        serializer = ProfessorSerializer(professors, many=True)
        return Response(serializer.data)
