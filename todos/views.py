from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from todos.serializers import TodoSerializer
from rest_framework import permissions, filters
from todos.models import Todo
from django_filters.rest_framework import DjangoFilterBackend

class TodoAPIView(ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id', 'title', 'is_complete']
    search_fields = ['id', 'title','is_complete']
    order_fields = ['id', 'title','is_complete']


    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)
    
class TodoDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class=TodoSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)
    