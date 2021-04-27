from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Course
from .serializers import CourseSerializer

class CourseView(APIView):

    def get(self, request):
        serializer = CourseSerializer(Course.objects.all(), many=True)
        response = {"course": serializer.data}
        return Response(response, status=status.HTTP_200_OK)
