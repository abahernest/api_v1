from django.conf.urls import url
from .views import UserCreate

urlpatterns = [
    url(r'signup', UserCreate.as_view(), name='account-create'),
]
