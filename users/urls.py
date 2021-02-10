from knox import views as knox_views
from .views import RegisterAPI,LoginAPI
from django.urls import path

urlpatterns = [
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('signup/', RegisterAPI.as_view(), name='register'),
]
