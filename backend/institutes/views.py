from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Institute
from .serializers import InstiSerializer
from django.core.cache import cache
import re

class InstituteAPIView(APIView):

    def get(self, request):
        serializer = InstiSerializer(Institute.objects.all(), many=True)
        response = {"institutes": serializer.data}
        return Response(response, status=status.HTTP_200_OK) 


class InstituteDetailAPIView(APIView):

    def get(self, request, insti_id_val):
        serializer = InstiSerializer(Institute.objects(insti_id = insti_id_val), many=True)
        response = {"institute": serializer.data}
        return Response(response, status=status.HTTP_200_OK)

class InstituteExamAPIView(APIView):

    def get(self, request, insti_name_val):
        exams_covered = []
        for institute in Institute.objects(insti_name = insti_name_val):
            exams_covered = institute.insti_exams_covered

        response = {"exams_covered": exams_covered}
        return Response(response, status=status.HTTP_200_OK)

class InstituteLikeAPIView(APIView):

    def get(self, request, insti_name_val):
        regex_val = re.compile('.*'+insti_name_val+'*',re.IGNORECASE)
        serializer = InstiSerializer(Institute.objects(insti_name = regex_val), many=True)
        response = {"institute": serializer.data}
        return Response(response, status=status.HTTP_200_OK)