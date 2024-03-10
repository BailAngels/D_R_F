from django.urls import path

from lessons.views import (
    students, create_student, detail_student,
)

urlpatterns = [
    path('students/', students),
    path('students/<int:pk>', detail_student),
    path('create/', create_student),
]
