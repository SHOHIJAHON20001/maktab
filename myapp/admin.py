from django.contrib import admin
from django.contrib.auth.models import Group
from myapp.models import School


admin.site.unregister([Group])

class schoolAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'age', 'student_class', 'created_at']

admin.site.register(School, schoolAdmin)
