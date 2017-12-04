from django.shortcuts import render
from rest_framework.response import Response
from buildings.models import SimpleApartment
from buildings.serializers import SimpleApartmentSerializer
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def get_simple_apartment_info(request, apartment_id):
	apartment = SimpleApartment.objects.get(id=apartment_id)
	return Response(SimpleApartmentSerializer(apartment).data)
