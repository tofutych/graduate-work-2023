from django.contrib.auth.models import User
from django.db import models
from faculties.models import Faculty


class Enrollee(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    faculty = models.ForeignKey(
        Faculty, related_name="applicants", on_delete=models.CASCADE
    )

    surname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True)
    certificate = models.ImageField(upload_to="uploads/", blank=True, null=True)
    special_rights = models.ImageField(upload_to="uploads/", blank=True, null=True)
    disability = models.ImageField(upload_to="uploads/", blank=True, null=True)

    def __str__(self):
        return f"{self.id} {self.name}"

    def get_absolute_url(self):
        return f"faculties/{self.faculty.id}/applicants/{self.id}/"

    def get_images(self):
        answer = []
        if self.certificate:
            answer.append("http://127.0.0.1:8000" + self.certificate.url)
        if self.special_rights:
            answer.append("http://127.0.0.1:8000" + self.special_rights.url)
        if self.disability:
            answer.append("http://127.0.0.1:8000" + self.disability.url)
        return answer

    def is_staff(self):
        return self.user.is_staff


class Achievement(models.Model):
    enrollee = models.ForeignKey(
        Enrollee, related_name="achievements", on_delete=models.CASCADE)

    title = models.CharField(max_length=255, null=True)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(null=True)
    url = models.URLField(max_length=255, null=True)
    date_added = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="uploads/", blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"{self.enrollee.get_absolute_url()}achievement/{self.id}/"

    def get_image(self):
        if self.image:
            return "http://127.0.0.1:8000" + self.image.url
        return ""
