from rest_framework import serializers
from .models import Student, School


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'first_name',
            'last_name',
            'student_identification',
            'school'
        )
        model = Student
class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'max_students',
        )
        model = School