from rest_framework import serializers

from .models import Achievement, Enrollee


class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = (
            "enrollee",
            "id",
            "title",
            "description",
            "date",
            "url",
            "image",
            "get_image",
            "get_absolute_url",
        )


class EnrolleeSerializer(serializers.ModelSerializer):
    achievements = AchievementSerializer(many=True)

    class Meta:
        model = Enrollee
        fields = (
            "id",
            "faculty",
            "surname",
            "name",
            "patronymic",
            "date_of_birth",
            "get_images",
            "achievements",
            "get_absolute_url",
            "is_staff",
        )
