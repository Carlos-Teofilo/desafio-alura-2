from django.db import models

# Create your models here.
class Receita(models.Model):
    descricao = models.TextField(blank=False, null=False)
    valor = models.IntegerField(blank=False, null=False)
    data = models.DateField(blank=False, null=False)

    def __str__(self):
        return self.descricao


class Despesa(models.Model):
    descricao = models.TextField(blank=False, null=False)
    valor = models.IntegerField(blank=False, null=False)
    data = models.DateField(blank=False, null=False)

    def __str__(self):
        return self.descricao
