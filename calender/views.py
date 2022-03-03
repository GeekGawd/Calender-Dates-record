from django.shortcuts import render
from rest_framework import generics
from . import models, serializers

# Create your views here.
class Relapse(generics.ListAPIView):
    queryset = models.Calender.objects.all()
    serializer_class = serializers.RelapseSerializer
    