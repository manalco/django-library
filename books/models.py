from django.db import models
from django.core.validators import MinValueValidator


class Book(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField(max_length=2000)
	author = models.CharField(max_length=255)
	stock = models.PositiveIntegerField(default=2, validators=[MinValueValidator(1)]) # Always leave a copy on the library

	def __str__(self):
		return self.name