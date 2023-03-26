from django.contrib import admin

from . models import Position,Employee

# Register your models here.

admin.site.register(Position)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id','fullname','emp_code','mobile','position')

admin.site.register(Employee,EmployeeAdmin)