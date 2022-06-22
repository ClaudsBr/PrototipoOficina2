
# Univesp  
  ## Projeto Integrador em Computação II-Turma 001
## GERAL-PJI240-SALA-001GRUPO-047
 
   
### Integrantes:  
  
* Abraão George Halcsik
* Adriana Aparecida de Souza Turetti        
* Aline Souza Alves         
* Andressa Aparecida Silva de Souza      
* Claudio Oliveira dos Santos            
* Rafael de Araújo Macedo   
* Valdeir Braz de Souza     
* Vilma Maria do Nascimento         
  
  
  
### Objetivo do Projeto:  
  
Desenvolver uma Aplicação Web em Python com o framework Django e o Banco de Dados MySQL que permite fazer o cadastro e login dos clientes de uma Oficina Mecânica 
<h3 align="center">Sistema de Login e Cadastro de Clientes de Oficina Mecânica</h3>


<h4> Pagina Inicial da Aplicação</h4>




```bash
localhost:8000/
``` 

<img src="https://user-images.githubusercontent.com/65355088/175037385-5817b03b-ca2c-4bcd-b1f8-e847f0d61157.jpg" width=60%>
<img src="https://user-images.githubusercontent.com/65355088/175037386-bb24f657-70c4-4f9b-804e-e12d47fe5ad7.jpg" width=60%>
<img src="https://user-images.githubusercontent.com/65355088/175037389-81807a1c-21dc-42df-b3af-6435f4277286.jpg" width=60%>
<img src="https://user-images.githubusercontent.com/65355088/175037391-2b093e05-3a5e-4731-9596-313ba7f9d8bf.jpg" width=60%>

* Clicando em <b>Fale Conosco </b><br>
 ```bash
localhost:8000/contato/
``` 
<img src="https://user-images.githubusercontent.com/65355088/175037359-b0f4a0c2-44c5-4eb2-ba8a-619cc2162094.jpg" width=60%>
<img src="https://user-images.githubusercontent.com/65355088/175037362-85b01eec-0a56-4781-a61f-e2c3fd88ffab.jpg" width=60%>

* Clicando em <b>Area do Cliente </b>(Acesso Não permitido sem efetuar login)<br>

 ```bash
localhost:8000/dashboard/
``` 
<img src="https://user-images.githubusercontent.com/65355088/175037274-9e2537fd-f0d5-4672-850c-62967cbb5283.jpg" width=60%>

<h4>Registrando Usuário</h4>
Clicando em <b>Registrar Usuario </b><br>


 ```bash
localhost:8000/create/
``` 


<img src="https://user-images.githubusercontent.com/65355088/175037396-28765a3b-8838-4ea9-a389-48b002f286a5.jpg" width=60%>

Preenchendo os Campos<br>
<img src="https://user-images.githubusercontent.com/65355088/175037399-e20a30be-8b87-44dc-a0f7-de59d3d1d4b0.jpg" width=60%>

Usuário Registrado com Sucesso!<br>
<img src="https://user-images.githubusercontent.com/65355088/175037397-3939f1a4-13d7-4bb9-9fa8-5b6de12e40a8.jpg" width=60%>

<h4> Efetuando Login</h4><br>
<img src="https://user-images.githubusercontent.com/65355088/175037394-38f2d8aa-049e-4781-a0b9-0269f6a0b9ca.jpg" width=60%>

<h4> Acessando Area do Cliente</h4>
Usuario Logado<br>
<img src="https://user-images.githubusercontent.com/65355088/175037354-29edf173-998e-4ce0-820b-bfa43c8f4958.jpg" width=60%>

<h4> Area Administrativa</h4>
Permitida apenas para o perfil <b>admin</b>, onde fica a parte <b>CRUD </b>da Aplicação

 ```bash
localhost:8000/administrador/index
``` 
Exibe os Clientes cadastrados e permite <b>operações de Cadastrar, Editar, Visualizar e Deletar</b> clientes
<img src="https://user-images.githubusercontent.com/65355088/175037264-79c9e426-c6d5-4bd9-a555-da2e8e6d9015.jpg" width=60%><br>
<b>Cadastrando um novo Cliente</b> (botão Cadastrar Cliente)

Abre-se o formulario para<b> inserção dos Dados Cadastrais do Cliente</b><br>
 ```bash
localhost:8000/usuario/formulario
``` 
<img src="https://user-images.githubusercontent.com/65355088/175037367-3aca4731-40f4-4d44-8b05-ddfafdd73f99.jpg" width=60%><br>

 Preenchendo os Campos<br>
 <img src="https://user-images.githubusercontent.com/65355088/175037370-b8beedb7-cbb6-40c1-bd36-19869157c51d.jpg" width=60%><br>
 
 Apos Salvar os Dados do Cliente irá se abrir o formulario para <b>preenchimento do Endereço </b>do Cliente<br>
 ```bash
localhost:8000/usuario/endereco
``` 
 <img src="https://user-images.githubusercontent.com/65355088/175037371-4cbb39e6-dd66-4f2d-aaa4-f637928ea380.jpg" width=60%><br>
 
  Preenchendo os campos<br>
  <img src="https://user-images.githubusercontent.com/65355088/175037374-ef988b25-1ac0-47bd-b4b2-56475c8e5d3e.jpg" width=60%><br>
  
 Apos a inserção do Endereço irá se abrir o formulario para <b>preenchimento dos dados do Veiculo</b><br>
 ```bash
localhost:8000/usuario/veiculo/
``` 
 <br>
 
 <img src="https://user-images.githubusercontent.com/65355088/175037378-cc56fd55-6953-4fbf-b2c7-2757db01e6da.jpg" width=60%><br>
 
 Preenchendo os campos<br>
 <img src="https://user-images.githubusercontent.com/65355088/175037382-dc74c202-738a-4376-bac4-7863a7969240.jpg" width=60%><br>
 
 Apos preencher os dados do Veiculo será redirecionado à Area Administrativa com o novo usuario inserido
 
 <img src="https://user-images.githubusercontent.com/65355088/175037268-f35a3454-250e-48cf-ba70-2652cbec2ec7.jpg" width=60%><br>
 <br>
 <h3><b> Editando Dados do Cliente</h3></b><br>
 Antes da Edição<br>
 <img src="https://user-images.githubusercontent.com/65355088/175133094-9f42ac7f-8374-4e3d-ad7e-e5049ac28639.jpg" width=60%><br>
 Formulario de Edição do Cliente Selecionado<br>
 <img src="https://user-images.githubusercontent.com/65355088/175135799-a3944ed8-c0a3-45ce-90eb-c474564d966f.jpg" width=60%><br>
 Alterações feitas no Cadastro do Cliente<br>
 <img src="https://user-images.githubusercontent.com/65355088/175135804-bab8aa4e-88d1-472f-95c9-fae2244a50be.jpg" width=60%><br>
 Dados modificados no Painel Administrativo
 <img src="https://user-images.githubusercontent.com/65355088/175135806-fd031dfb-2584-4b08-8051-8d8b7f5fb360.jpg" width=60%><br>
 <h3><b>Vizualizando Dados Cliente</b></h3> <br><br>
 <img src="https://user-images.githubusercontent.com/65355088/175037272-e5b878f0-1a39-47e0-9c9f-cdedfce10368.jpg" width=60%><br>
 <br>
 <h3><b>Deletando Cliente</b></h3> <br><br>
 Antes da Deleção<br>
 <img src="https://user-images.githubusercontent.com/65355088/175133088-b82a514d-05d8-43eb-b609-48e11bd154bc.jpg" width=60%><br>
 <br>
 Clicando no botão Deletar o Ajax emite um pop-up de confirmação<br>
 <img src="https://user-images.githubusercontent.com/65355088/175133096-5a8c4a3f-b8e1-4f81-9138-a2758ef49342.jpg" width=60%><br>
 <br>
 Após confirmar a deleção do Cliente<br>
 <img src="https://user-images.githubusercontent.com/65355088/175133094-9f42ac7f-8374-4e3d-ad7e-e5049ac28639.jpg" width=60%><br>
  
## Referências:  
  
* <a href="https://webdesignemfoco.com/cursos/python">CRUD em Python & Cadastro e Login com Python</a>
* <a href="https://docs.python.org/pt-br/3.8/contents.html">Documentação do Python 3.8</a>
* <a href="https://docs.djangoproject.com/pt-br/4.0">Documentação do Django Framework</a>
* <a href="https://getbootstrap.com.br/docs/4.1/getting-started/introduction/">Documentação do Bootstrap</a>
* <a href="https://www.devmedia.com.br/exemplo/documentacao-de-css/56">Documentação do CSS</a>





<h3 align="left">Contatos:</h3>

  * Abraão George Halcsik - <b>Email: 2005323@aluno.univesp.br</b><br>
* Adriana Aparecida de Souza Turetti - <b>Email: 2001824@aluno.univesp.br</b><br>
* Aline Souza Alves - <b>Email: 2013591@aluno.univesp.br</b><br>
* Claudio Oliveira dos Santos - <b>Email: 2009814@aluno.univesp.br</b><br>
* Valdeir Braz de Souza - <b>Email: 2015625@aluno.univesp.br</b><br>
  
  
  
<h3 align="left">Linguagens e Ferramentas:</h3>  
<p align="left"> <a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a> <a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> <img src="https://www.svgrepo.com/show/353657/django-icon.svg" alt="django" width="40" height="40"/> </a> <a href="https://git-scm.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a> <a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a> <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="40" height="40"/> </a> <a href="https://www.mysql.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg" alt="mysql" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>
