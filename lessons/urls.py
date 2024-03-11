from django.urls import path

from lessons.views import (
    lesson_list,
    lesson_create,
    lesson_update,
    lesson_patrial_update,
    lesson_delete
)

urlpatterns = [
    path('lessons/', lesson_list),
    path('lessons/<int:pk>/', lesson_list),
    path('lessons/create/', lesson_create),
    path('lessons/update/<int:pk>/', lesson_update),
    path('lessons/pr-update/<int:pk>/', lesson_patrial_update),
    path('lessons/delete/<int:pk>/', lesson_delete)
]
