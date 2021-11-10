from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Teacher


def index(request):
    return render(request, 'main/index.html')


def teachers_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'main/teachers.html', {"title": "Main Teachers", "teachers_list": teachers})


def faculty_group(request):
    return render(request, 'main/faculty.html')





















