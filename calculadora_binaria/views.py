from rest_framework import viewsets

from calculadora_binaria import models, serializer


class CalculadoraViewSet(viewsets.ModelViewSet):
    queryset = models.Calculadora.objects.all()
    serializer_class = serializer.CalculadoraSerializer
