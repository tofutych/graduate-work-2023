from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Faculty, Speciality
from .serializers import (FacultyListSerializer, FacultySerializer,
                          SpecialitySerializer)


class FacultyList(APIView):
    def get(self, request, format=None):
        faculties = Faculty.objects.all()
        serializer = FacultyListSerializer(faculties, many=True)
        return Response(serializer.data)


class FacultyDetail(APIView):
    def get_object(self, id):
        try:
            return Faculty.objects.get(id=id)
        except Faculty.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        faculty = self.get_object(id)
        serializer = FacultySerializer(faculty)
        return Response(serializer.data)


class SpecialityList(APIView):
    def get(self, request, faculty_slug, format=None):
        specialities = Speciality.objects.filter(faculty__slug=faculty_slug)
        serializer = SpecialitySerializer(specialities, many=True)
        return Response(serializer.data)
