from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('profile/', profile, name="profile"),
    path('authorization/', authorization, name="authorization"),
    path('registration/', registration, name="registration"),
    path('about/', about, name="about")
]