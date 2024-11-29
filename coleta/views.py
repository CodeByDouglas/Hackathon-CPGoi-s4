from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Coleta_Organica, Coleta_Seletiva

class ConsultaColetaOrganica(APIView):
    def get(self, request, cep):
        coleta = Coleta_Organica.objects.filter(cep_inicio__lte=cep, cep_fim__gte=cep).first()
        if coleta:
            return Response({
                "dia_semana": coleta.dia_semana,
                "turno": coleta.turno,
                "cep_inicio": coleta.cep_inicio,
                "cep_fim": coleta.cep_fim,
            })
        return Response({"Desculpe não consegui entender localizar seu endereço, verifica o seu CEP e reenvia para min por favor."}, status=404)
    
class ConsultaColetaSeletiva(APIView):
        def get(self, request, cep):
            coleta = Coleta_Seletiva.objects.filter(cep_inicio__lte=cep, cep_fim__gte=cep).first()
            if coleta:
             return Response({
                "dia_semana": coleta.dia_semana,
                "turno": coleta.turno,
                "cep_inicio": coleta.cep_inicio,
                "cep_fim": coleta.cep_fim,
            })
            return Response({"Desculpe não consegui entender localizar seu endereço, verifica o seu CEP e reenvia para min por favor."}, status=404)
