from django.db import models
from django_extensions.db.models import TimeStampedModel

# Create your models here.


class Roles(TimeStampedModel):
	active = models.BooleanField(default=True)
	name = models.CharField(max_length=100, null=False)

	def __str__(self):
		return self.name