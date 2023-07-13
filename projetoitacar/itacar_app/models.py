from distutils.archive_util import make_zipfile
from xml.parsers.expat import model
# biblioteca do Django para trabalhar com o banco de dados
from django.db import models
from django.forms import CharField, Field
from django.utils import timezone
import datetime


#Model Criar Usuário Motorista
class UsuarioMotorista(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    nomeMot = models.CharField(max_length=235)
    nomeDoCarro = models.CharField(max_length=235)
    placaDoCarro = models.CharField(max_length=235)
    classificacaoEstrelas = models.IntegerField(default=0)
    CPF = models.CharField(max_length=235)

#def consultar_email(self, email):
#def consultar_password(self, email):

#Model Passageiro
class Passageiro(models.Model):
    nomePass = models.CharField(max_length=235)
    CPF = models.CharField(max_length=235)
    telefone = models.CharField(max_length=235)
    # notaAvaliacao = models.IntegerField()


#Model Avaliação Passageiro
class Avaliacao(models.Model):
    idCorrida = models.IntegerField()
    nomePass = models.CharField(max_length=255)
    nota = models.IntegerField()
    comentario = models.TextField()

    def avaliarPassageiro(self):
        self.save()


#Model HistoricoViagem
class HistoricoViagem(models.Model):
    IDMotorista = models.CharField(max_length=100)
    IDpassageiro = models.CharField(max_length=100)
    data = models.DateField()
    horario = models.TimeField()
    valorViagem = models.DecimalField(max_digits=8, decimal_places=2)


#Model RelatorioFinanceiro
class RelatorioFinanceiro(models.Model):
    data = models.DateField()
    valor_recebido_total = models.DecimalField(max_digits=10, decimal_places=2)
    taxa_do_app = models.DecimalField(max_digits=10, decimal_places=2)
    gasto_medio_gasolina = models.DecimalField(max_digits=10, decimal_places=2) 
    
    
class Viagem(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    nomePass = models.CharField(max_length=235)
    nomeMot = models.CharField(max_length=235)