from django.urls import path
from .views import ConsultaColetaOrganica, ConsultaColetaSeletiva, ConsultaEcoPontos, Entrada_de_menssagem, Eviar_mensagens



urlpatterns = [
    path('consulta-organica/<str:cep>/', ConsultaColetaSeletiva.as_view(), name='consulta_coleta_organica'),
    path('consulta-seletiva/<str:cep>/', ConsultaColetaOrganica.as_view(), name='consulta_coleta_seletiva'),
    path('consulta-ecoponto/', ConsultaEcoPontos.as_view(), name='consulta_coleta_seletiva'),
    path('webhook/', Entrada_de_menssagem.as_view(), name='webhook'),
    path('enviar-mensagem/', Eviar_mensagens.as_view(), name='enviar_mensagem'),  # Corrigido
]
