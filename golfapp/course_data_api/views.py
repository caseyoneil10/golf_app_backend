from django.shortcuts import render

from rest_framework import generics
from .serializers import CourseSerializer
from .models import Course

class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all().order_by('name')
    serializer_class = CourseSerializer

class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all().order_by('name')
    serializer_class = CourseSerializer
