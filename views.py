from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from .models import Tasks
from .serializer import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [OrderingFilter]
    filter_fields = ['category']  # Allow filtering by category
