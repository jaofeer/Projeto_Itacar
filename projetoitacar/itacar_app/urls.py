#aqui são configurados os namespaces da app web que o Django usará para fazer o 
#roteamento entre das URLs às respectivas funções do controle (definidas no arquivo views.py) 
from django.urls import path
#importação das funções do fluxo de controle da app controle_bancario_app que estão definidas no arquivo views.py
from itacar_app import views

#dependendo da quantidade de casos de uso, você precisa associar a função no fluxo de controle
#  (definidas em views.py) à interface (página html).
#Você precisa criar um path para que o Django possa fazer o roteamento das URLs às respectivas
# funções do controle (definidas no arquivo views.py) 
urlpatterns = [
    #Quando o usuário estiver na página web inicial "", o Django redirecionará o controle para 
    # a função home definida em views.py.
    path("", views.home, name="home"),
    path("criarConta/", views.criarConta, name="criarConta"),
    path("efetuarLogin/", views.efetuarLogin, name="efetuarLogin"),
    path("historicoCorrida/", views.historicoCorrida, name="historicoCorrida"),
    path("avaliarPassageiro/", views.avaliarPassageiro, name="avaliarPassageiro"),
    path("relatorioFinanceiro/", views.relatorioFinanceiro, name="relatorioFinanceiro"),
]