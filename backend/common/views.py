from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from institutes.models import Institute
from .serializers import InstiSerializer
from django.core.cache import cache


class SearchAPIView(APIView):

    def get(self, request):
        serializer = InstiSerializer(Institute.objects.all(), many=True)
        response = {"institutes": serializer.data}
        return Response(response, status=status.HTTP_200_OK) 

