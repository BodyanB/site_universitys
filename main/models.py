from django.db import models


class University(models.Model):
    name = models.CharField(max_length=64)


class Faculty(models.Model):
    name = models.CharField(max_length=64)


class Specialty(models.Model):
    name = models.CharField(max_length=64)


class Group(models.Model):
    name = models.CharField(max_length=64)


class Student(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    group = models.CharField(max_length=64)


class Teacher(models.Model):
    name = models.CharField('Name', max_length=64)
    surname = models.CharField('SurName', max_length=64)
    faculty = models.CharField(max_length=64)

    def __str__(self):
        return self.name

