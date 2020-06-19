from django.db import models


class Empresa(models.Model):
    cnpj = models.CharField(max_length=20)
    nome_fantasia = models.CharField(max_length=50)
    razao_social = models.CharField(max_length=200)
    telefone = models.CharField(max_length=15)
    dominio = models.CharField(max_length=50)


class GrupoDeTrabalho(models.Model):
    nome = models.CharField(max_length=50)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)


class Relatorio(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.CharField(max_length=300)
    url = models.CharField(max_length=200)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    grupo_de_trabalho = models.ForeignKey(GrupoDeTrabalho, on_delete=models.CASCADE)


class UsuarioVsRelatorio(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    grupo_de_trabalho = models.ForeignKey(GrupoDeTrabalho, on_delete=models.CASCADE)

