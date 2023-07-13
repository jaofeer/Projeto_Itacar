from datetime import datetime  #biblioteca python para trabalhar com datas
import random #biblioteca python para gerar numeros aleatorios
from http import client #biblioteca python para fazer conexão com um nó cliente. Esse nó seria o navegador do usuário final do nosso sistema
from django.shortcuts import render #biblioteca do django para enviar respostas usando o protocolo http
from django.shortcuts import redirect #biblioteca do django para redirecionar de uma interface web (página web) para outra - cria a navegação entre páginas web
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password
from .models import UsuarioMotorista, Avaliacao, HistoricoViagem, RelatorioFinanceiro


#View Home
def home(request):
    #método executado quando o usuário está na interface (paǵina html) inicial do sistema  home.html
    return render(request, "ita_car/home.html")


#View Criar Conta
def criarConta(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        # idMot = request.POST['idMot']
        nomeMot = request.POST['nomeMot']
        nomeDoCarro = request.POST['nomeDoCarro']
        placaDoCarro = request.POST['placaDoCarro']
        classificacaoEstrelas = 0
        CPF = request.POST['CPF']
        
        
        hashed_password = make_password(password)
        
        user = UsuarioMotorista(
            email=email, 
            password=hashed_password,
            nomeMot=nomeMot, 
            nomeDoCarro=nomeDoCarro, 
            placaDoCarro=placaDoCarro,
            classificacaoEstrelas=classificacaoEstrelas,
            CPF=CPF)
        user.save()
        
        return redirect('/efetuarLogin/')
    
    return render(request, 'ita_car/criarConta.html')


#View Efetuar Login
def efetuarLogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        try:
            user = UsuarioMotorista.objects.get(email=email)
            if check_password(password, user.password):
                # Autenticação bem-sucedida
                return redirect('/')
            else:
                # Senha incorreta
                error_message = 'Senha incorreta. Tente novamente.'
        except UsuarioMotorista.DoesNotExist:
            # Usuário não encontrado
            error_message = 'Usuário não encontrado. Tente novamente.'
        
        return render(request, 'ita_car/efetuarLogin.html', {'error_message': error_message})
    
    return render(request, 'ita_car/home.html')


#View Avaliar Passageiro
def avaliarPassageiro(request):
    if request.method == 'POST':
        idCorrida = request.POST.get('idCorrida')
        nomePass = request.POST.get('nomePass')
        nota = request.POST.get('nota')
        comentario = request.POST.get('comentario')

        if idCorrida and nomePass and nota and comentario:
            avaliacao_obj = Avaliacao(idCorrida = idCorrida, nomePass = nomePass, nota = nota, comentario = comentario)
            avaliacao_obj.save()
            return render(request, "ita_car/avaliarPassageiro.html")
        else:
            return HttpResponse("Por favor, preencha todos os campos obrigatórios.")
    
    return render(request, "ita_car/avaliarPassageiro.html")



#View Historico Corrida
def historicoCorrida(request):
    historico = HistoricoViagem.objects.all()
    return render(request, 'ita_car/historicoCorrida.html', {'historico': historico} )

#View Relatório Financeiro
def relatorioFinanceiro(request):
    relatorios = RelatorioFinanceiro.objects.all()
    return render(request, 'ita_car/relatorioFinanceiro.html', {'relatorios': relatorios})

