from rest_framework.test import APITestCase
from django.urls import reverse
from task_.models import User, Task

class TaskTests(APITestCase):
    def test_task_public(self):
        User.objects.create_user(username='evg', password='123') # с заглавной, т.к обращаемся к базе данных
        Task.objects.create(title='test-title', public=True, user_id=1)
        Task.objects.create(title='test-title', public=False, user_id=1)
        response = self.client.get(reverse('task:public'))   # reverse строит относительный путь от сервера
        # print(reverse('task:public'))
        # print(response.data)
        self.assertEqual(1, len(response.data))