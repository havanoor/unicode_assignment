from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


class EmployeeInline(admin.StackedInline):
    model=Employee
    can_delete=False
    verbose_name_plural='employee'


class UserAdmin(BaseUserAdmin):
    inlines=(EmployeeInline,)


# Register your models here.
admin.site.register(Employee)
admin.site.register(Jobs)
admin.site.register(MonthlyExpense)
admin.site.register(MonthlySaving)
admin.site.register(YearlyExpenditure)
admin.site.register(YearlySaving)
admin.site.register(Balance)

admin.site.unregister(User)
admin.site.register(User,UserAdmin)
