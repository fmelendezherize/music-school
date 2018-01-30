# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.response import Response
from rest_framework import status
from .models import Course
from .serializers import CourseSerializer, CourseWriteSerializer

# Create your views here.
class CourseList(APIView):
    def get(self, request, format=None):
        courses = Course.objects.all()
        #Must have its own serializer
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CourseWriteSerializer(data=request.data)
        if serializer.is_valid():
            the_response = CourseSerializer(serializer.save())
            return Response(the_response.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
