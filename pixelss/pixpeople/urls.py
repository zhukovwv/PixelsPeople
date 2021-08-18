from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('profile/<int:profid>', profile),
    path('authorization', authorization),
    path('registration', registration)
]