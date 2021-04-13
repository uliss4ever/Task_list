from django.urls import path
from .views import *

urlpatterns = [
    path('create/task', TaskCreateView.as_view()),
    path('create/comment/', CommentCreateView.as_view()),
    path('all/', TaskListView.as_view()),
    path('details/<int:pk>', TaskItemView.as_view()),


]