from django.shortcuts import render
from myapp.models import School

def school(requests):

    students = School.objects.all()

    context= {
        "students":students,
    }

    return render(requests, "index.html", context)
