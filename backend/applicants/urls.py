from django.urls import path

from applicants import views

from .models import Achievement

urlpatterns = [
    path(
        "faculties/<int:faculty_id>/applicants/", views.EnrolleeByFacultyList.as_view()
    ),
    path(
        "faculties/<slug:faculty_slug>/applicants/",
        views.EnrolleeByFacultySlugList.as_view(),
    ),
    path(
        "faculties/<int:faculty_id>/applicants/<int:enrollee_id>/",
        views.EnrolleeDetail.as_view(),
    ),
    path(
        "faculties/<int:faculty_id>/applicants/<int:enrollee_id>/achievements/",
        views.AchievementsByEnrolleeList.as_view(),
    ),
    path("applicants/", views.EnrolleeByTokenDetail.as_view()),
    path("applicants/<int:id>/", views.EnrolleeByIdDetail().as_view()),
    path("achievements/<int:id>/", views.AchievementDetail().as_view()),
]
