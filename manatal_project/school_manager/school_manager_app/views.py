from django.shortcuts import render

from rest_framework import generics, permissions

from .models import Student, School
from .serializers import StudentSerializer, SchoolSerializer
from rest_framework.response import Response



class ListStudent(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def create(self, request, *args, **kwargs):
        """
        verify that the POST has the request user as the obj.author
        """
        print(request.data["school"])
        school=School.objects.get(pk=request.data["school"])
        if Student.objects.filter(school=school).count()>=school.max_students:
            return Response(status=403)
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=201, headers=headers)



class DetailStudent(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class ListSchool(generics.ListCreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class DetailSchool(generics.RetrieveUpdateDestroyAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer