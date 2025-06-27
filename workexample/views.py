from rest_framework import viewsets
from .models import WorkExample
from .serializers import WorkExampleSerializer

class WorkExampleViewSet(viewsets.ModelViewSet):
    queryset = WorkExample.objects.all()
    serializer_class = WorkExampleSerializer