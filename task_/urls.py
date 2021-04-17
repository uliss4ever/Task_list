from django.urls import path
from .views import *

app_name = 'task'
urlpatterns = [
    path('', TaskCreateView.as_view(), name='create'),
    path('comment/', CommentCreateView.as_view(), name='comment'),
    path('public/', TaskListView.as_view(), name='public'),
    path('details/<int:pk>', TaskItemView.as_view(), name='details'),
    path('owner/', TaskOwnerListView.as_view(), name='owner')

]
