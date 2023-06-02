from django.urls import path

from faculties import views

urlpatterns = [
    path("faculties/", views.FacultyList.as_view()),
    path("faculties/<int:id>/", views.FacultyDetail.as_view()),
    path("<slug:faculty_slug>/specialities/", views.SpecialityList.as_view()),
]
