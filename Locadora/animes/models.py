from django.db import models
from uuid import uuid4


class Animes(models.Model):
    id_anime = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    titulo = models.CharField(max_length=100)
    episodios = models.IntegerField()
    autor = models.CharField(max_length=100)
    Ano_de_lancamento = models.IntegerField()
