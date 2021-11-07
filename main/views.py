from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def index(request):
    return render(request, 'main/index.html')


def faculty_group(request):
    return render(request, 'main/faculty.html')





















