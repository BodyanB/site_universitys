
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('faculty_group', views.faculty_group, name='faculty'),
    path('teachers_list', views.teachers_list, name='teachers'),
]