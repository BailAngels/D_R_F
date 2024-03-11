from django.urls import path

from homeworks.views import (
    fruits_list,
    fruits_create,
    fruits_delete,
    fruits_update,
    fruits_patrial_update
)

urlpatterns = [
    path('fruits/', fruits_list),
    path('fruits/<int:pk>/', fruits_list),
    path('fruits/create/', fruits_create),
    path('fruits/update/<int:pk>/', fruits_update),
    path('fruits/pr-update/<int:pk>/', fruits_patrial_update),
    path('fruits/delete/<int:pk>/', fruits_delete)
]