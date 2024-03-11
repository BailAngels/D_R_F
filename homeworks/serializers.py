from rest_framework import serializers

from homeworks.models import Fruits


class FruitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fruits
        fields = (
            'id',
            'title',
            'price'
        )
