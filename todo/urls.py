from django.urls import path
from .views import *

urlpatterns =[
    path('todo/',TodoListView.as_view()),
    path('todo/<int:pk>/',TodoDetailView.as_view()),
    path('todo/<str:type>/', TodoCalandarView.as_view()),
   
]