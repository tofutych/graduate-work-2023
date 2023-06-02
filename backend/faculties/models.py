from django.db import models


class Faculty(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        db_table = "faculties"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/{self.slug}/"


class Speciality(models.Model):
    faculty = models.ForeignKey(
        Faculty, related_name="specialities", on_delete=models.CASCADE
    )

    name = models.CharField(max_length=255)
    code = models.CharField(max_length=64)
    slug = models.SlugField()

    class Meta:
        db_table = "specialties"

    def __str__(self):
        return self.name
