from rest_framework import serializers


class StudentSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField()
    age = serializers.IntegerField()
    is_genius = serializers.BooleanField()


class FruitSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField()
    price = serializers.IntegerField()
