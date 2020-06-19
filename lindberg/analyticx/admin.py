from django.contrib import admin

from .models import Empresa, GrupoDeTrabalho, Relatorio, UsuarioVsRelatorio

admin.site.register(Empresa)
admin.site.register(GrupoDeTrabalho)
admin.site.register(Relatorio)
admin.site.register(UsuarioVsRelatorio)
