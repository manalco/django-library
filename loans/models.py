from django.db import models
from django.core.exceptions import ValidationError
from django.contrib import admin
from django.contrib import messages
from django.contrib.auth.models import User
from datetime import date

from books.models import Book


class Loan(models.Model):
	student = models.ForeignKey(User, related_name='loans', on_delete=models.CASCADE, limit_choices_to={'groups__name': "Student"})
	book = models.ForeignKey('books.Book', null=True, related_name='loans', on_delete=models.CASCADE)
	subject = models.ForeignKey('subjects.Subject', null=False, related_name='loans', on_delete=models.CASCADE)
	loan_starts = models.DateField(default=date.today)
	loan_ends = models.DateField(default=date.today)
	return_date = models.DateField(null=True, blank=True, editable=False)
	status = models.BooleanField(default=True, verbose_name='Loan is active', help_text='If the loan is active, the book is in the student\'s custody.')
	notes = models.TextField(max_length=4000, null=True, blank=True)


	def clean(self):
		errors = []
		user_loan_queryset = Loan.objects.filter(student=self.student, book=self.book, status=True)
		user_loan = user_loan_queryset.last()

		# Making sure it is possible to update loans
		if user_loan_queryset.count() > 0 and user_loan and user_loan.pk != self.pk:
			errors.append(ValidationError("User ("+self.student.username+") has an active loan with a copy of this book."))

		if self.return_date:
			errors.append(ValidationError("This loan has been returned and cannot be updated."))
		if self.loan_starts >= self.loan_ends:
			errors.append(ValidationError("Loan end date must be after the start date."))
		if self.book.stock <= 1:
			errors.append(ValidationError("There is not enough stock of this book to loan."))
		if errors:
			raise ValidationError(errors)


	def save(self, *args, **kwargs):
		book = Book.objects.get(pk=self.book.pk)
		loan = Loan.objects.filter(pk=self.pk)

		if loan and loan.first().status == True and self.status == False:
			book.stock += 1
			self.return_date = date.today()
		else:
			book.stock -= 1

		book.save()
		return super(Loan, self).save(*args, **kwargs)


	def __str__(self):
		status = ' ACTIVE '
		if self.return_date:
			status = 'RETURNED'
		return '['+status+'] ['+self.student.username+'] '+self.book.name
