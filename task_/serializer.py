from rest_framework import serializers
from .models import Task, Comment

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
    # task_types = serializers.SlugRelatedField(queryset=TaskType.objects.all(), slug_field="name", required=False)
    date_add = serializers.DateTimeField(format='%d/%m/%Y %H:%M:%S', input_formats=['%d/%m/%Y %H:%M:%S'], required=False)
    comments = CommentSerializer(many=True, required=False)

    class Meta:
        model = Task
        fields = "__all__"


class TaskListSerializer(serializers.ModelSerializer):
    # task_types = serializers.SlugRelatedField(slug_field='name', read_only=True) # чтобы вместо цифр (тип) были слова
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
    # реализована логика автоматической проверки формата входных данных
    important = serializers.BooleanField(required=False)
    public = serializers.BooleanField(required=False)
    # task_types = serializers.SlugRelatedField(slug_field='name', queryset=TaskType.objects.all(), required=False)
    ACTIVE_ST = 'A'
    HIDDEN_ST = "H"
    DONE_ST = 'D'
    STATUS_CHOICES = [
        (ACTIVE_ST, 'Активно'),
        (HIDDEN_ST, 'Отложено'),
        (DONE_ST, 'Выполнено'),
    ]
    task_types = serializers.ChoiceField(choices=STATUS_CHOICES, required=False)