from django.contrib import admin
from .models import Loan

@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    readonly_fields = ["return_date"]


##admin.site.register(Loan)