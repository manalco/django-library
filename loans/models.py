from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Loan(models.Model):
	notes = models.TextField(max_length=4000, null=True)
	subject = models.ForeignKey('subjects.Subject', related_name='loans', on_delete=models.CASCADE)
	book = models.ForeignKey('books.Book', null=True, related_name='loans', on_delete=models.CASCADE)
	loan_start = models.DateField(default=date.today)
	loan_ends = models.DateField(default=date.today)
	student = models.ForeignKey(User, related_name='loans', on_delete=models.CASCADE)
	created_by = models.ForeignKey(User, related_name='+', on_delete=models.CASCADE)