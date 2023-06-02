from rest_framework import serializers

from .models import Faculty, Speciality


class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = (
            "id",
            "name",
            "code",
            "slug",
        )


class FacultySerializer(serializers.ModelSerializer):
    specialities = SpecialitySerializer(many=True)

    class Meta:
        model = Faculty
        fields = (
            "id",
            "name",
            "slug",
            "get_absolute_url",
            "specialities",
        )


class FacultyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = (
            "id",
            "name",
            "slug",
            "get_absolute_url",
        )
