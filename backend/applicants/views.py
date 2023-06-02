from django.contrib.auth.models import User
from django.http import Http404
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Achievement, Enrollee
from .serializers import AchievementSerializer, EnrolleeSerializer


class EnrolleeByFacultyList(APIView):
    def get(self, request, faculty_id, format=None):
        applicants = Enrollee.objects.filter(faculty__id=faculty_id)
        serializer = EnrolleeSerializer(applicants, many=True)
        return Response(serializer.data)


class EnrolleeByFacultySlugList(APIView):
    def get(self, request, faculty_slug, format=None):
        applicants = Enrollee.objects.filter(faculty__slug=faculty_slug)
        serializer = EnrolleeSerializer(applicants, many=True)
        return Response(serializer.data)


class EnrolleeDetail(APIView):
    def get_object(self, id):
        try:
            return Enrollee.objects.get(id=id)
        except Enrollee.DoesNotExist:
            raise Http404

    def get(self, request, faculty_id, enrollee_id, format=None):
        enrollee = self.get_object(enrollee_id)
        serializer = EnrolleeSerializer(enrollee)
        return Response(serializer.data)


class EnrolleeByTokenDetail(APIView):
    def post(self, request, format=None):
        user_id = Token.objects.get(key=request.data["token"]).user_id
        enrollee = Enrollee.objects.get(user__id=user_id)
        serializer = EnrolleeSerializer(enrollee)
        print(serializer.data)
        return Response(serializer.data)


class EnrolleeByIdDetail(APIView):
    def get_object(self, id):
        try:
            return Enrollee.objects.get(id=id)
        except Enrollee.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        enrollee = self.get_object(id)
        serializer = EnrolleeSerializer(enrollee)
        return Response(serializer.data)


class AchievementsByEnrolleeList(APIView):
    def get(self, request, faculty_id, enrollee_id, format=None):
        achievements = Achievement.objects.filter(enrollee__id=enrollee_id)
        serializer = AchievementSerializer(achievements, many=True)
        return Response(serializer.data)

    def post(self, request, faculty_id, enrollee_id, format=None):
        serializer = AchievementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AchievementsByTokenList(APIView):
    def post(self, request, format=None):
        serializer = AchievementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AchievementDetail(APIView):
    def get_object(self, id):
        try:
            return Achievement.objects.get(id=id)
        except Group.DoesNotExist:
            raise Http404

    def delete(self, request, id, format=None):
        achievement = self.get_object(id)
        achievement.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
