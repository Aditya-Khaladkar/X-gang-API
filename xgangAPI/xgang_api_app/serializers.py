# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from .models import xgang

# Create a model serializer
class xgangSerial(serializers.HyperlinkedModelSerializer):
	# specify model and fields
	class Meta:
		model = xgang
		fields = ('id', 'name', 'chutyap', 'githubLink')
