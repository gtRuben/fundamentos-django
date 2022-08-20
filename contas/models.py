from tabnanny import verbose
from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=80)
    dt_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Transacao(models.Model):
    data = models.DateTimeField()
    titulo = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    observacao = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Transações'

    def __str__(self):
        return self.titulo