from django.db import models
from django_extensions.db.models import TimeStampedModel

# Create your models here.


class Organizations(TimeStampedModel):
	name = models.CharField(max_length=100, null=False)
	key = models.CharField(max_length=20, null=False, unique=True)
	valid_up_to = models.DateTimeField(null=False)
	max_user_licenses = models.IntegerField(null=False)
	max_buildings_licenses = models.IntegerField(null=False)

	def __str__(self):
		return self.name



