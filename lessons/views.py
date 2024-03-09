from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from lessons.serializers import StudentSerializer, FruitSerializer


students_list = [
    {'id': 1, 'name': 'Erbol', 'age': 25, "is_genius": False},
    {'id': 2, 'name': 'Sardor', 'age': 35, "is_genius": False},
    {'id': 3, 'name': 'Halil', 'age': 5, "is_genius": False},
]


@api_view(http_method_names=['GET'])
def students(request: Request):
    serializer = StudentSerializer(data=students_list, many=True)
    if serializer.is_valid():
        return Response(serializer.data, status=200)
    else:
        return Response({'error': "No Validate Data"}, status=404)


@api_view(http_method_names=['POST'])
def create_student(request: Request):
    data = request.data
    print(data)
    students_list.append(data)
    return Response(students_list, status=201)


@api_view(http_method_names=['GET'])
def detail_student(request: Request, pk: int):
    student = [i for i in students_list if i['id'] == pk]
    data = StudentSerializer(data=student).initial_data
    return Response(data, status=200)


fruits_list = [
    {'id': 1, 'name': 'Apple', 'price': 100},
    {'id': 2, 'name': 'Strawberry', 'price': 110},
    {'id': 3, 'name': 'Pear', 'price': 200},
]


@api_view(http_method_names=['GET'])
def fruits(request: Request):
    serializer = FruitSerializer(data=fruits_list, many=True)
    if serializer.is_valid():
        return Response(serializer.data, status=200)
    else:
        return Response({'error': 'No Validate Data'}, status=404)


@api_view(http_method_names=['POST'])
def create_fruit(request: Request):
    data = request.data
    fruits_list.append(data)
    return Response(fruits_list, status=201)


@api_view(http_method_names=['GET'])
def detail_fruit(request: Request, pk: int):
    fruit = [i for i in fruits_list if i['id'] == pk]
    data = FruitSerializer(data=fruit).initial_data
    return Response(data, status=200)