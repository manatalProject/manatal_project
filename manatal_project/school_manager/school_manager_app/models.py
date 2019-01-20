from django.db import models
from django.utils.crypto import get_random_string

class School(models.Model):
    name= models.CharField(max_length=20)
    max_students=models.PositiveIntegerField(default = 3 )

    def __str__(self):
        return (self.name)

class Student(models.Model):
    first_name= models.CharField(max_length=20)
    last_name= models.CharField(max_length=20)
    student_identification = models.CharField(max_length=20, default =get_random_string(length=10), editable=False)
    school= models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return (self.first_name)