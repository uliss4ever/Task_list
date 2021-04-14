from rest_framework import serializers
from .models import Task, TaskType, Comment

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)
    date_add = serializers.DateTimeField(format='%d/%m/%Y %H:%M:%S', input_formats=['%d/%m/%Y %H:%M:%S'])
    class Meta:
        model = Comment
        fields = "__all__"

class CommentCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Comment
        fields = "__all__"

class TaskItemSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)
    # определяем выводимый формат поля таск-тайпс
    # task_types = serializers.CharField(source='get_task_types_display')
    task_types = serializers.SlugRelatedField(queryset=TaskType.objects.all(), slug_field="name", required=False)
    date_add = serializers.DateTimeField(format='%d/%m/%Y %H:%M:%S', input_formats=['%d/%m/%Y %H:%M:%S'], required=False)
    comments = CommentSerializer(many=True, required=False)

    class Meta:
        model = Task
        fields = "__all__"


class TaskListSerializer(serializers.ModelSerializer):
    task_types = serializers.SlugRelatedField(slug_field='name', read_only=True) # чтобы вместо цифр (тип) были слова
    date_add = serializers.DateTimeField(format='%d/%m/%Y %H:%M:%S', input_formats=['%d/%m/%Y %H:%M:%S'])
    user = serializers.SlugRelatedField(slug_field="username", read_only=True) # по id юзера заменяем на имя

    class Meta:
        model = Task
        # fields = ('id', 'title',)
        fields = "__all__"


class TaskCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Task
        # fields = "__all__"
        exclude = ["date_add", "task_types", ]

class QuerySerializer(serializers.Serializer):
    important = serializers.BooleanField()
    public = serializers.BooleanField()
    task_types = serializers.SlugRelatedField(slug_field='name', queryset=TaskType.objects.all(), required=False)