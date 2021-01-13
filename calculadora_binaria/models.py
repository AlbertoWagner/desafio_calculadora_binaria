from django.db import models

from calculadora_binaria.choices import C_OPERACAO


class Calculadora(models.Model):
    numero_1 = models.TextField(null=False, max_length=255)
    numero_2 = models.TextField(null=False, max_length=255)
    operador = models.IntegerField(choices=C_OPERACAO)
    resultado = models.TextField(null=True, max_length=255)

    class Meta:
        db_table = 'calculadora'

    def __str__(self):
        return '%s' % self.resultado
