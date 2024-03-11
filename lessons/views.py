from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from lessons.serializers import LessonSerializer
from lessons.models import Lesson


@api_view(http_method_names=['GET'])
def lesson_list(request: Request, pk=None):
    if pk:
        data = Lesson.objects.get(pk=pk)
        serializer = LessonSerializer(instance=data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    # Делаем ОРМ запрос
    data = Lesson.objects.all()
    # Преобразуем данные в JSON
    serializer = LessonSerializer(instance=data, many=True)
    # Возвращаем наши данные
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(http_method_names=['POST'])
def lesson_create(request: Request):
    title, subject, plan = request.data['title'], request.data['subject'], request.data['plan']
    data = Lesson.objects.create(title=title, subject=subject, plan=plan)
    serializer = LessonSerializer(instance=data)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(http_method_names=['PUT'])
def lesson_update(request: Request, pk):
    title, subject, plan = request.data['title'], request.data['subject'], request.data['plan']

    data = Lesson.objects.get(id=pk)
    data.title = title
    data.subject = subject
    data.plan = plan
    data.save()
    serializer = LessonSerializer(instance=data)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(http_method_names=['PATCH'])
def lesson_patrial_update(request: Request, pk):
    try:
        title = request.data['title']
    except KeyError:
        title = None

    try:
        subject = request.data['subject']
    except KeyError:
        subject = None

    try:
        plan = request.data['plan']
    except KeyError:
        plan = None

    data = Lesson.objects.get(id=pk)

    if title:
        data.title = title
        data.save()

    if subject:
        data.subject = subject
        data.save()

    if plan:
        data.plan = plan
        data.save()

    serializer = LessonSerializer(instance=data)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(http_method_names=['DELETE'])
def lesson_delete(request: Request, pk):
    lesson = Lesson.objects.get(id=pk)
    lesson.delete()

    data = Lesson.objects.all()
    serializer = LessonSerializer(instance=data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
