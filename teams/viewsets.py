from rest_framework import viewsets
from .models import Teams
from .serializers import TeamsSerializer

class TeamsViewSet(viewsets.ModelViewSet):
    queryset = Teams.objects.all()
    serializer_class = TeamsSerializer