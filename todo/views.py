from rest_framework import generics
from .models import Todo
from rest_framework.response import Response
from .serializers import TodoSerializer
from rest_framework.views import APIView
from .models import Todo
from .serializers import TodoSerializer
from datetime import date


class TodoListView (generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoDetailView (generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoCalandarView (APIView):

    def get (self,request,type,format=None):
        if type =='day':
            todo = Todo.objects.filter(date=date.today())
            serializer = TodoSerializer(todo,many=True)
            return Response(serializer.data)
        elif type =='month':
            return Response ({"title":"Month Selected"})
        elif type == 'week':
            return Response ({"title":"week Selected"})