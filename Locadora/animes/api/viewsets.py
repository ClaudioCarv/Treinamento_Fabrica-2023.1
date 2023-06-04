from rest_framework import viewsets
from animes.api import serializers
from animes import models

class AnimesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AnimesSerializer
    queryset = models.Animes.objects.all()