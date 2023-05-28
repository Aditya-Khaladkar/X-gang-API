from django.shortcuts import render, HttpResponse
from rest_framework import viewsets

from .serializers import xgangSerial
from .models import xgang

# create a viewset
class XgangViewSet(viewsets.ModelViewSet):
	# define queryset
	queryset = xgang.objects.all()
	
	# specify serializer to be used
	serializer_class = xgangSerial
