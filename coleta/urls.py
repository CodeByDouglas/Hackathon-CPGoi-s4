from django.urls import path
from .views import ConsultaColetaOrganica
from .views import ConsultaColetaSeletiva



urlpatterns = [
    path('consulta-organica/<str:cep>/', ConsultaColetaSeletiva.as_view(), name='consulta_coleta_organica'),
    path('consulta-seletiva/<str:cep>/', ConsultaColetaOrganica.as_view(), name='consulta_coleta_seletiva'),
]
