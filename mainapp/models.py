from django.db import models
from django.utils import timezone


# creating the school model


class School(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    create_at = models.DateTimeField(default=timezone.now())
    update_at = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.name


# creating the student model
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    enrollment = models.CharField(max_length=100, unique=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    create_at = models.DateTimeField(default=timezone.now())
    update_at = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.name
