from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Loan(models.Model):
	student = models.ForeignKey(User, related_name='loans', on_delete=models.CASCADE, limit_choices_to={'groups__name': "Student"})
	book = models.ForeignKey('books.Book', null=True, related_name='loans', on_delete=models.CASCADE)
	subject = models.ForeignKey('subjects.Subject', null=False, related_name='loans', on_delete=models.CASCADE)
	loan_starts = models.DateField(default=date.today)
	loan_ends = models.DateField(default=date.today)
	notes = models.TextField(max_length=4000, null=True)
