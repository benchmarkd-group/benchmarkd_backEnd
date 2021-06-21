from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Course
from .serializers import CourseSerializer
from django.core.cache import cache

class CourseView(APIView):
    def get(self, request):
        serializer = CourseSerializer(Course.objects.all(), many=True)
        response = {"courses": serializer.data}
        return Response(response, status=status.HTTP_200_OK)

class CourseDetailAPIView(APIView):
    def get(self, request,course_id_val):
        serializer = CourseSerializer(Course.objects(course_id = course_id_val), many=True)
        response = {"course": serializer.data}
        return Response(response, status=status.HTTP_200_OK)
