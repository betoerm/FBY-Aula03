from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    idade = models.IntegerField(default=1)
    data_nascimento = models.DateField(null=True)
    cpf  = models.CharField(max_length=14, default='00000000000')

class Endereco(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    logradouro = models.CharField(max_length=200)
    numero =  models.IntegerField(default=1)
    cep = models.CharField(max_length=200)
    bairro = models.CharField(max_length=200, default="Centro")

class Departamento(models.Model):
    nome = models.CharField(max_length=200)    

class Cargo(models.Model):
    nome = models.CharField(max_length=200)