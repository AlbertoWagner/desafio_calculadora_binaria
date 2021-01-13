from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from calculadora_binaria.models import Calculadora

# variáveis globais

url_calculadora_binaria = 'http://127.0.0.1:8000/calculadora_binaria/'


class CalculadoraTestCase(APITestCase):
    """ Teste com usuário adm ,
     crud categotia [PUT,POST,GET,DELETE] """

    def setUp(self):
        self.client = APIClient()

    def teste_soma(self):
        data = {
            "numero_1": "00000001",
            "numero_2": "00000011",
            "operador": 3,
        }
        self.response = self.client.post(url_calculadora_binaria, data)
        self.assertEquals(Calculadora.objects.all().count(), 1)
        self.assertEquals(Calculadora.objects.all()[0].resultado, '00000100')
        Calculadora.objects.all()[0].delete()

    def teste_subtracao(self):
        data = {
            "numero_1": "00000010",
            "numero_2": "00000001",
            "operador": 4,
        }
        self.response = self.client.post(url_calculadora_binaria, data)
        self.assertEquals(Calculadora.objects.all().count(), 1)
        self.assertEquals(Calculadora.objects.all()[0].resultado, '00000001')
        Calculadora.objects.all()[0].delete()

    def teste_modulo(self):
        data = {
            "numero_1": "00010100",
            "numero_2": "00000011",
            "operador": 5,
        }
        self.response = self.client.post(url_calculadora_binaria, data)
        self.assertEquals(Calculadora.objects.all().count(), 1)
        self.assertEquals(Calculadora.objects.all()[0].resultado, '00000010')
        Calculadora.objects.all()[0].delete()

    def teste_multiplicacao(self):
        data = {
            "numero_1": "00000010",
            "numero_2": "00000011",
            "operador": 2,
            "resultado": "00000110"
        }
        self.response = self.client.post(url_calculadora_binaria, data)
        self.assertEquals(Calculadora.objects.all().count(), 1)
        self.assertEquals(Calculadora.objects.all()[0].resultado, '00000110')
        Calculadora.objects.all()[0].delete()

    def teste_divisao(self):
        data = {
            "numero_1": "00001010",
            "numero_2": "00000010",
            "operador": 1,
        }
        self.response = self.client.post(url_calculadora_binaria, data)
        self.assertEquals(Calculadora.objects.all().count(), 1)
        self.assertEquals(Calculadora.objects.all()[0].resultado, '00000101')
        Calculadora.objects.all()[0].delete()
