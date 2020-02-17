from rest_framework import viewsets
from .models import Loan
from .serializer import LoanSerializer


class LoanViewSet(viewsets.ModelViewSet):
	queryset = Loan.objects.all()
	serializer_class = LoanSerializer

	# To display only loans that belong to the current user
	# def get_queryset(self):
	#	if self.request.user.pk == 1:
	#		response = Loan.objects.all()
	#	else:
	#		response = Loan.objects.filter(student=self.request.user)
	#
	#	return response
