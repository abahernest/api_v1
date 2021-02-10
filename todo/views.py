from rest_framework import generics,status,permissions
from .models import Todo
from rest_framework.response import Response
from .serializers import TodoSerializer
from rest_framework.views import APIView
from .models import Todo
from .serializers import TodoSerializer
from datetime import date



class TodoListView (generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoDetailView (generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoCalandarView (APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get (self,request,type,format=None):
        if type =='day':
            todo = Todo.objects.filter(date_created=date.today())
            serializer = TodoSerializer(todo,many=True)
            return Response(serializer.data)
        # elif type =='month':
        #     month = date.today().month
        #     year = date.today().year
        #     todo = Todo.objects.get(date_created__contains=f"2020-02")
        #     serializer = TodoSerializer(todo,many=True)
        #     return Response(serializer.data)
        # elif type == 'week':
        #     return Response ({"title":"week Selected"})
        else:
            return Response({"message":"Not Found"},status=status.HTTP_404_NOT_FOUND)
