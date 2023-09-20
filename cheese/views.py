from .models import Cheese
from rest_framework import viewsets, permissions
from .serializers import CheeseSerializer

class CheeseViewSet(viewsets.ModelViewSet):
  # The main query for the index route, queryset is a list of all Cheese objects
  queryset = Cheese.objects.all()
  # Serializer class for serializing output, used to control which serializer class should be used for serializing and deserializing queryset and model instances
  serializer_class = CheeseSerializer
  # Optional permission class set permission level
  permission_classes = [permissions.AllowAny]