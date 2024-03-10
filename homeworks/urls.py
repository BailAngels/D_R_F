from django.urls import path

from homeworks.views import (
    fruits, detail_fruit, create_fruit
)


urlpatterns = [
    path('fruits/', fruits),
    path('fruits/<int:pk>', detail_fruit),
    path('create_fruit/', create_fruit),
]
