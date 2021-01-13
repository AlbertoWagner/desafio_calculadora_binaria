from django.urls import path

from calculadora_binaria import views

app_name = 'calculadora'

urlpatterns = [

    path('calculadora/', views.CalculadoraViewSet.as_view(), name='calculadora'),

]