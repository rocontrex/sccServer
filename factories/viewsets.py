from rest_framework import viewsets
from .models import Factories
from .serializers import FactorySerializer

class FactoryViewSet(viewsets.ModelViewSet):
    queryset = Factories.objects.all()
    serializer_class = FactorySerializer