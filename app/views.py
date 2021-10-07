from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from app.models import TodoList
from app.serializers import TodoListSerializer
from django_filters.rest_framework import DjangoFilterBackend


class TodoListViewSet(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ('id', 'name', 'done')
    filterset_fields = ('id', 'name')


# The version  bellow is a way to build crud using generic libraries.

"""

class TodoListViews(generics.ListCreateAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ('id', 'name', 'done')
    filterset_fields = ('id', 'name')


class TodoListChangeDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer


# The version  bellow is a standard way to build crud,
# without using generic libraries.
"""

# The version  bellow is a standard way to build crud,
# without using generic libraries.

"""
class TodoListViews(APIView):

    @staticmethod
    def get(request):
        todo = TodoList.objects.all()
        serializer = TodoListSerializer(todo, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def post(request):
        serializer = TodoListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoListChangeDelete(APIView):
    serializer_class = TodoListSerializer

    def get_object(self, pk):
        try:
            return TodoList.objects.get(id=pk)
        except TodoList.DoesNotExist:
            return NotFound()

    def get(self, request, pk):
        todo = self.get_object(pk)
        serializer = TodoListSerializer(todo)
        return Response(serializer.data)

    def put(self, request, pk):
        todo = self.get_object(pk)
        serializer = TodoListSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        todo = self.get_object(pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""

