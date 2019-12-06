from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Employee)
admin.site.register(Jobs)
admin.site.register(MonthlyExpense)
admin.site.register(MonthlySaving)
admin.site.register(YearlyExpenditure)
admin.site.register(YearlySaving)
admin.site.register(Balance)