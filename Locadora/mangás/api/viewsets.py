from rest_framework import viewsets
from mangás.api import serializers
from mangás import models

class MangasViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MangasSerializer
    queryset = models.Mangas.objects.all()