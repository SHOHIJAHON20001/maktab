from django.contrib import admin
from django.contrib.auth.models import Group
from myapp.models import School


admin.site.unregister([Group])
admin.site.register([School])
