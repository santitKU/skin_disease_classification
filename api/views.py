from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Disease
from api.serializers import DiseaseSerializer
from rest_framework import generics

# Create your views here.

class DiseaseList(generics.ListAPIView):
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer

class DiseaseDetail(generics.RetrieveAPIView):
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer