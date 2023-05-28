from rest_framework import serializers

from .models import xgang

class xgangSerial(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = xgang
		fields = ('id', 'name', 'chutyap', 'githubLink')
