from rest_framework import serializers

from calculadora_binaria import models
from calculadora_binaria.models import Calculadora

simbolos = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'


class CalculadoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Calculadora

        fields = ('id', 'numero_1', 'numero_2', 'operador', 'resultado')

    def converter(self, n, base, simbolos):
        if base < 0 or base > len(simbolos):
            raise ValueError('base inválida')
        result = []
        while n > 0:
            result.insert(0, simbolos[n % base])
            n //= base
        return ''.join(result)

    def operacao(self, numero_1, numero_2, operador):
        if (operador == 1):
            return numero_1 / numero_2
        elif (operador == 2):
            return numero_1 * numero_2
        elif (operador == 3):
            return numero_1 + numero_2
        elif (operador == 4):
            return numero_1 - numero_2
        elif (operador == 5):
            return numero_1 % numero_2

    def create(self, validated_data):
        numero_1 = int(validated_data['numero_1'], 2)
        numero_2 = int(validated_data['numero_2'], 2)
        operador = int(validated_data['operador'])
        valor = int(self.operacao(numero_1, numero_2, operador))
        resultado = '%.8s' % (str(str(self.converter(valor, 2, simbolos))).rjust(8, '0'))
        calculadora_binaria = Calculadora.objects.create(numero_1=validated_data['numero_1'],
                                                         operador=validated_data['operador'],
                                                         numero_2=validated_data['numero_2'],
                                                         resultado=resultado)
        return calculadora_binaria
