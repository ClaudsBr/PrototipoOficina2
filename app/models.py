from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=150)
    cpf = models.CharField('CPF', max_length=20)
    rg = models.CharField('RG', max_length=15)
    data_nasc = models.DateField('Data de Nascimento')
    telefone = models.CharField('Telefone', max_length=15)
    email = models.EmailField('Email', max_length=50, null=True, blank=True)


class Endereco(models.Model):
    rua = models.CharField('Rua', max_length=150)
    numero = models.IntegerField()
    complemento = models.CharField('Complemento', max_length=120, null=True, blank=True)
    cep = models.CharField('Cep', max_length=9)
    bairro = models.CharField( max_length=100)
    cidade = models.CharField('Cidade', default='Itapevi', max_length=50)


class Veiculo(models.Model):
    modelo = models.CharField('Modelo', max_length=50)
    marca = models.CharField('Marca', max_length=20)
    ano = models.IntegerField()
    cor = models.CharField(max_length=50)
    placa = models.CharField(max_length=7)



class Agendamento(models.Model):
    HORARIO_CHOICES = [
        (8, '8:00'),
        (9, '9:00'),
        (10, '10:00'),
        (11, '11:00'),
        (12, '12:00'),
        (13, '13:00'),
        (14, '14:00'),
        (15, '15:00'),
        (16, '16:00'),
        (17, '17:00'),
        (18, '18:00'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_insp = models.DateField('Data da Inspeção')
    horario = models.IntegerField('Horario da Inspeção', choices=HORARIO_CHOICES)
    descricao = models.TextField('Descrição do Problema')
    def __str__(self):
        return self.cliente