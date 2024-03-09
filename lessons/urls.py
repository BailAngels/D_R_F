from django.urls import path

from lessons.views import (
    students, create_student, detail_student,
    fruits, create_fruit, detail_fruit
)

urlpatterns = [
    path('students/', students),
    path('students/<int:pk>', detail_student),
    path('create/', create_student),

    path('fruits/', fruits),
    path('fruits/<int:pk>', detail_fruit),
    path('create_fruit/', create_fruit),
]
