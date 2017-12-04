from rest_framework import serializers
from buildings.models import SimpleApartment

class SimpleApartmentSerializer(serializers.ModelSerializer):

	class Meta:
		model = SimpleApartment
		fields = ('id', 'name', 'price')
