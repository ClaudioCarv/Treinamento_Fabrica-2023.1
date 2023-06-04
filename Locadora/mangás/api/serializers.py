from rest_framework import serializers
from mangás import models


class MangasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Mangas
        fields = '__all__'