from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from calculadora_binaria.models import Calculadora


# Register your models here.

admin.site.register(Calculadora)
