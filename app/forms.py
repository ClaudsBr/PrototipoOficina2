from django.forms import ModelForm
from app.models import Cliente, Endereco, Veiculo

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'cpf', 'rg', 'data_nasc', 'telefone', 'email']

class EnderecoForm(ModelForm):
    class Meta:
        model = Endereco
        fields = ['rua', 'numero', 'complemento', 'cep', 'bairro', 'cidade']

class VeiculoForm(ModelForm):
    class Meta:
        model = Veiculo
        fields = ['modelo', 'marca', 'ano', 'cor', 'placa']