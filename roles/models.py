from django.db import models
from django_extensions.db.models import TimeStampedModel

# Create your models here.


class Roles(TimeStampedModel):
	ORGANIZATION_ADMIN = 'organization_admin'
	SELLER = 'seller'

	active = models.BooleanField(default=True)
	key = models.CharField(max_length=20,unique=True)
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name