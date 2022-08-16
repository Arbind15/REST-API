from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=500)
    roll_number = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100)

    def __str__(self):
        return self.name
