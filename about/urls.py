from django.urls import path
from .views import *

urlpatterns = [
    path('', About.as_view()),
]