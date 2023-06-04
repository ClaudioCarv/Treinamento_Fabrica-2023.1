from django.db import models

from uuid import uuid4


class Mangas(models.Model):
    id_anime = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    titulo = models.CharField(max_length=100)
    capitulos = models.IntegerField()
    autor = models.CharField(max_length=100)
    Ano_de_lancamento = models.IntegerField()
