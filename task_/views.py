from datetime import datetime

from django.shortcuts import render, get_object_or_404
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


from .models import Task
from .permissions import IsOwnerOrReadOnly
from .serializer import *

class TaskItemView(APIView):   # работаем с имеющейся записью (получение, удаление, изменение)
    permission_classes = [IsOwnerOrReadOnly]
    def get(self, request, pk):
        task = get_object_or_404(Task, id=pk)
        serializer = TaskItemSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        task = get_object_or_404(Task.objects.filter(id=pk))
        change_task = TaskItemSerializer(instance=task, data=request.data, partial=True)
        if change_task.is_valid():  # из модели
            change_task.save()
            return Response(change_task.data, status=status.HTTP_200_OK)
        else:
            return Response(change_task.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = get_object_or_404(Task.objects.filter(id=pk))
        task.delete()
        return Response(pk, status=status.HTTP_200_OK)



class TaskListView(APIView):    # в дженериках - отдельный класс "создать" и в нём только метод post
    def get(self, request, **kwargs):
        # tasks = Task.objects.all().order_by('-important', '-date_add')
        tasks = Task.objects.filter(public=True).order_by('-important', '-date_add')

        query_params = QuerySerializer(data=request.query_params, partial=True)
        if query_params.is_valid():
            if query_params.data.get('important'):
                tasks = tasks.filter(important=query_params.data.get('important'))
            if query_params.data.get('public'):
                tasks = tasks.filter(public=query_params.data.get('public'))
            if query_params.data.get('task_types'):
                task_types = get_object_or_404(TaskType, name=query_params.data.get('task_types'))
                if task_types:
                    tasks = tasks.filter(task_types=task_types.id)
        else:
            return Response(query_params.errors, status=status.HTTP_400_BAD_REQUEST)


        serializer = TaskListSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TaskOwnerListView(APIView):    # в дженериках - отдельный класс "создать" и в нём только метод post
    def get(self, request, **kwargs):
        tasks = Task.objects.filter(user=request.user).order_by('-important', '-date_add')

        query_params = QuerySerializer(data=request.query_params, partial=True)
        if query_params.is_valid():
            if query_params.data.get('important'):
                tasks = tasks.filter(important=query_params.data.get('important'))
            if query_params.data.get('public'):
                tasks = tasks.filter(public=query_params.data.get('public'))
            if query_params.data.get('task_types'):
                task_types = get_object_or_404(TaskType, name=query_params.data.get('task_types'))
                if task_types:
                    tasks = tasks.filter(task_types=task_types.id)
        else:
            return Response(query_params.errors, status=status.HTTP_400_BAD_REQUEST)


        serializer = TaskListSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class TaskCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data
        serializer = TaskCreateSerializer(data=data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        data['date_add'] = datetime.today()
        serializer = CommentCreateSerializer(data=data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # TODO methods