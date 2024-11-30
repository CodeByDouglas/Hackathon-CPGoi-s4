from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Coleta_Organica, Coleta_Seletiva, Eco_pontos
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from twilio.rest import Client
import os
import coleta.FucEnvio as envio_mensagem
from .FucEnvio import envio_mensagem



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
        return Response({"Desculpe não cosegui localizar seu endereço, O CEP deve estar no formato XXXXX-XXX."}, status=404)
    
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
            return Response({"Desculpe não cosegui localizar seu endereço, O CEP deve estar no formato XXXXX-XXX."}, status=404)

class ConsultaEcoPontos(APIView):
    def get(self, request):
        coleta = Eco_pontos.objects.all()
        if coleta.exists():
            response_data = []
            for item in coleta:
                response_data.append({
                    "Nome": item.Nome,
                    "Dias_funcionamento": item.Dias_funcionamento,
                    "Horario_funcionamento": item.Horario_funcionamento,
                    "endereco": item.endereco,
                    "cep": item.cep,
                })
            return Response(response_data)
        return Response({"Desculpe, não consegui localizar nenhum Eco Ponto."}, status=404)


class Entrada_de_menssagem (APIView):
    def post(self, request):
        # request (print(request.data))
        return Response({"msg": "ok"})




class Eviar_mensagens(APIView):
    def get(self, request, cep):
        coleta = Coleta_Organica.objects.filter(cep_inicio__lte=cep, cep_fim__gte=cep).first()
        
def enviar_mensagem(body, to):
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=body,
        to=to
    )

    return message.sid