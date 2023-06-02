from django.contrib import admin

from .models import Achievement, Enrollee


@admin.register(Enrollee)
class EnrolleeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
