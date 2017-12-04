from django.db import models
from django_extensions.db.models import TimeStampedModel
from organizations.models import Organizations

class ApartmentTypes(TimeStampedModel):

	name = models.CharField(max_length=100, null=False)

	def __str__(self):
		return self.name

class Buildings(TimeStampedModel):


	name = models.CharField(max_length=100, null=False)
	location = models.CharField(max_length=140, null=False)
	building_type = models.CharField(max_length=20)
	organization = models.ForeignKey(Organizations, null=False)

class Floors(TimeStampedModel):
	number = models.IntegerField(null=False)
	floor_type = models.CharField(max_length=100, null=False)
	building = models.ForeignKey(Buildings, null=False)



class Apartment(TimeStampedModel):
	key = models.CharField(max_length=20, null=False)
	price = models.DecimalField(max_digits=14, decimal_places=4, null=False)
	floor = models.ForeignKey(Floors, null=False)
	apartment_type = models.ForeignKey(ApartmentTypes, null=False)



class SimpleApartment(TimeStampedModel):
	name = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=14, decimal_places=4, null=False)

	def __str__(self):
		return self.name