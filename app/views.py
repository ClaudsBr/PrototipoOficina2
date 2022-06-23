from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from app.forms import ClienteForm, EnderecoForm, VeiculoForm, AgendamentoForm
from app.models import Cliente, Veiculo, Endereco
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    return render(request,'home.html')

def create(request):
    return render(request, 'create.html')

def store(request):
    data = {}
    if(request.POST['password'] != request.POST['repassword']):
        data['msg'] = 'As senhas digitadas são diferentes!'
        data['class'] = 'alert-danger'
    else:
        user = User.objects.create_user(request.POST['user'],request.POST['email'], request.POST['password'] )
        user.first_name = request.POST['name']
        user.last_name = request.POST['lastname']
        user.save()
        data['msg'] = 'Usuário cadastrado com Sucesso!'
        data['class'] = 'alert-success'
    return render(request, 'create.html', data)

#Formulario do painel de login
def painel(request):
    return render(request,'painel.html')

#Processamento do login
def logar(request):
    data = {}
    user = authenticate(username=request.POST['user'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('/dashboard/')
    else:
        data['msg'] = 'Usuario ou Senha Inválidos!'
        data['class'] = 'alert-danger'
        return render(request,'painel.html', data)

#Pagina Inicial do Dashboard
def dashboard(request):
    return render(request, 'dashboard/home.html')

#Logout do Sistema
def deslogar(request):
    logout(request)
    return redirect('/painel/')


#Alterar Senha

def senha(request):
    return render(request,'senha.html')

def changePassword(request):
    user = User.objects.get(email=request.user.email)
    user.set_password(request.POST['password'])
    user.save()
    logout(request)
    return redirect('/painel/')


def administrador(request):
    data = {}
    #data['cli'] = Cliente.objects.all()
    search = request.GET.get('search')
    if search:
        data['cli'] = Cliente.objects.filter(nome__icontains=search)
    else:
        data['cli'] = Cliente.objects.all()
    #all = Cliente.objects.all()
    #paginator = Paginator(all, 2)
    #pages = request.GET.get('page')
    #data['cli'] = paginator.get_page(pages)
    return render(request, 'administrador/index.html', data)

def usuario(request):
    data ={}
    data['cliente'] = ClienteForm()
    return render(request, 'usuario/formulario.html', data)

def contato(request):
    return render(request,'contato.html')

def endereco(request):
    data ={}
    data['endereco'] = EnderecoForm()
    return render(request, 'usuario/endereco.html', data)

def veiculo(request):
    data= {}
    data['veiculo'] = VeiculoForm()
    return render(request, 'usuario/veiculo.html', data)

def criarCliente(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid:
        form.save()
        return redirect( 'endereco')


def criarEndereco(request):
    form = EnderecoForm(request.POST or None)
    if form.is_valid:
        form.save()
        return redirect( 'veiculo')


def criarVeiculo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid:
        form.save()
        return redirect( 'admin')

def view(request, pk):
    data = {}
    data['db'] = Cliente.objects.get(pk=pk)
    data['end'] = Endereco.objects.get(pk=pk)
    data['vei'] = Veiculo.objects.get(pk=pk)
    return render(request, 'usuario/view.html', data)

def editCliente(request, pk):
    data = {}
    data['cli'] = Cliente.objects.get(pk=pk)
    data['cliente'] = ClienteForm(instance=data['cli'])
    '''data['en'] = Endereco.objects.get(pk=pk)
    data['endereco'] = EnderecoForm(instance=data['en'])
    data['ve'] = Veiculo.objects.get(pk=pk)
    data['veiculo] = VeiculoForm(instance=data['ve']'''
    return render(request, 'usuario/formulario.html', data)

def editEndereco(request):
    data = {}
    data['end'] = Endereco.objects.get(pk=pk)
    data['endereco'] = EnderecoForm(instance=data['end'])
    return render(request, 'usuario/endereco.html', data)

def editVeiculo(request):
    data = {}
    data['vei'] = Veiculo.objects.get(pk=pk)
    data['veiculo'] = VeiculoForm(instance=data['vei'])
    return render(request, 'usuario/veiculo.html', data)

def updateCliente(request, pk):
    data = {}
    data['cliente'] = Cliente.objects.get(pk=pk)
    form = ClienteForm(request.POST or None, instance=data['cliente'])
    if form.is_valid():
        form.save()
        return redirect('admin')

def updateEndereco(request, pk):
    data = {}
    data['endereco'] = Cliente.objects.get(pk=pk)
    form = EnderecoForm(request.POST or None, instance=data['endereco'])
    if form.is_valid():
        form.save()
        return redirect('admin')

def updateVeiculo(request, pk):
    data = {}
    data['veiculo'] = Cliente.objects.get(pk=pk)
    form = VeiculoForm(request.POST or None, instance=data['veiculo'])
    if form.is_valid():
        form.save()
        return redirect('admin')

def deleteCliente(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    endereco = Endereco.objects.get(pk=pk)
    veiculo = Veiculo.objects.get(pk=pk)
    cliente.delete()
    endereco.delete()
    veiculo.delete()
    return redirect('admin')
