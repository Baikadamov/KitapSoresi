from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('cats/<int:catid>/', categories),  # http://127.0.0.1:8000/library/cats/
]
