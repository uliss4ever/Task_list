from django.urls import path
from .views import *

app_name = 'task'
urlpatterns = [
    path('', TaskCreateView.as_view(), name='create'),
    path('comment/', CommentCreateView.as_view(), name='comment'),
    path('ispublic/', TaskListView.as_view(), name='public'),
    path('<int:pk>/', TaskItemView.as_view(), name='details'),
    path('isowner/', TaskOwnerListView.as_view(), name='owner')

]
