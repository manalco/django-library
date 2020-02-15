from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Loan(models.Model):
	created_by = models.ForeignKey(User, related_name='loans', on_delete=models.CASCADE, verbose_name='Librarian')
	created_at = models.DateTimeField(auto_now_add=True)
	from_date = models.DateField(default=date.today, verbose_name='Loan Start')
	to_date = models.DateField(default=date.today, verbose_name='Loan Ends')
	book = models.ForeignKey('books.Book', on_delete=models.CASCADE, verbose_name='Book Name')