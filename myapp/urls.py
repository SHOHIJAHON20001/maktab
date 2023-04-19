from django.urls import path
from myapp.views import school

urlpatterns = [
    path('', school),
]
