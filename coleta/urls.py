from django.urls import path
from .views import ConsultaColetaOrganica, ConsultaColetaSeletiva, ConsultaEcoPontos



urlpatterns = [
    path('consulta-organica/<str:cep>/', ConsultaColetaSeletiva.as_view(), name='consulta_coleta_organica'),
    path('consulta-seletiva/<str:cep>/', ConsultaColetaOrganica.as_view(), name='consulta_coleta_seletiva'),
    path('consulta-ecoponto/', ConsultaEcoPontos.as_view(), name='consulta_coleta_seletiva'),
]
