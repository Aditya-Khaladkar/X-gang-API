from django.shortcuts import render, HttpResponse

# Create your views here.
# import viewsets
from rest_framework import viewsets

# import local data
from .serializers import serializers
from .models import xgang

# create a viewset
class XgangViewSet(viewsets.ModelViewSet):
	# define queryset
	queryset = xgang.objects.all()
	
	# specify serializer to be used
	serializer_class = serializers
