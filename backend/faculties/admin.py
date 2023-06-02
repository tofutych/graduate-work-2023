from django.contrib import admin

from .models import Faculty, Speciality


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "code")
    prepopulated_fields = {
        "slug": ("name",)
    }  # slug - name, а не code, потому что у некоторых повторяется код
