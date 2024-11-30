from django.urls import path
from .views import ConsultaColetaOrganica, ConsultaColetaSeletiva, ConsultaEcoPontos, EnviarMensagem

urlpatterns = [
    path('consulta-organica/<str:cep>/', ConsultaColetaOrganica.as_view(), name='consulta_coleta_organica'),
    path('consulta-seletiva/<str:cep>/', ConsultaColetaSeletiva.as_view(), name='consulta_coleta_seletiva'),
    path('consulta-ecoponto/', ConsultaEcoPontos.as_view(), name='consulta_ecoponto'),
    path('enviar-mensagem/', EnviarMensagem.as_view(), name='enviar_mensagem'),
    path('webhook/', EnviarMensagem.as_view(), name='webhook'),
]
