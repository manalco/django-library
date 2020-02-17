from rest_framework import serializers
from .models import Loan

class LoanSerializer(serializers.ModelSerializer):
	book = serializers.CharField(source="book.name", read_only=True)

	class Meta:
		model = Loan
		fields = '__all__'

