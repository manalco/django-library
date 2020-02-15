from django.db import models
from django.contrib.auth.models import User


class Subject(models.Model):
	name = models.CharField(max_length=255, unique=True)
	description = models.TextField(max_length=2000)

	def __str__(self):
		return self.name