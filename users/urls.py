from .views import RegisterAPI
from django.urls import path

urlpatterns = [
    path('signup/', RegisterAPI.as_view(), name='register'),
]
