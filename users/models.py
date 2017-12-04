from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.core.exceptions import ValidationError

# Create your models here.



class User(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(max_length=255, unique=True, db_index=True)