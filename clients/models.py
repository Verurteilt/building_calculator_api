from django.db import models
from django_extensions.db.models import TimeStampedModel
from organizations.models import Organizations
from roles.models import Roles


class Clients(TimeStampedModel):
	email = models.CharField(max_length=100, unique=True)
	full_name = models.CharField(max_length=100, null=False)
	organization = models.ForeignKey(Organizations, null=False)
	role = models.ForeignKey(Roles, null=True)
	password = models.CharField(max_length=256, null=True)


	def __str__(self):
		return "{0} ({1})".format(self.full_name, self.email)