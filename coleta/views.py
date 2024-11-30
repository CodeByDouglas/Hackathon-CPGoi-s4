from twilio.rest import Client
import os
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Coleta_Organica, Coleta_Seletiva, Eco_pontos

estado_global = {}

def enviar_mensagem(mensagem, to):
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=mensagem,
        to=to
    )

    return message.sid

class Entrada_de_menssagem:
    def __init__(self, to):
        self.to = to
        if to not in estado_global:
            estado_global[to] = 'inicial'

    def receber_mensagem(self, mensagem):
        if estado_global[self.to] == 'inicial':
            self.enviar_mensagem_inicial()
            estado_global[self.to] = 'aguardando_resposta'
        elif estado_global[self.to] == 'aguardando_resposta':
            self.processar_resposta(mensagem)
        elif estado_global[self.to] == 'aguardando_cep':
            self.enviar_informacoes_coleta()

    def enviar_mensagem_inicial(self):
        mensagem = (
            "Oi! Eu sou o Zeco Lógico, assistente virtual do Governo de Goiás! "
            "Estou aqui para te ajudar com informações sobre a coleta de lixo e sustentabilidade na cidade. "
            "Vamos juntos fazer a diferença! 🌍 Me diz, no que posso ajudar?\n"
            "1) Saber sobre coleta seletiva.\n"
            "2) Saber sobre coleta de resíduos domiciliares.\n"
            "3) Encontrar ecopontos próximos.\n"
            "4) Fazer uma reclamação."
        )
        enviar_mensagem(mensagem, self.to)

    def processar_resposta(self, mensagem):
        if mensagem != '1':
            resposta = (
                "Legal! Para te passar informações certinhas sobre a coleta, como dias e horários no seu bairro, "
                "preciso que você me informe o seu CEP. Pode digitar aqui!"
            )
            enviar_mensagem(resposta, self.to)
            estado_global[self.to] = 'aguardando_cep'
        elif estado_global[self.to] == 'aguardando_cep':
            self.enviar_informacoes_coleta()
        else:
            resposta = "Desculpe, não entendi sua resposta. Por favor, escolha uma das opções: 1, 2, 3 ou 4."
            enviar_mensagem(resposta, self.to)

    def enviar_informacoes_coleta(self):
        resposta = (
            "Olha, verifiquei aqui no sistema e as coletas na sua região são realizadas "
            "as Terça-Feira, durante o período diurno. Se precisar de mais informações, é só avisar!"
        )
        enviar_mensagem(resposta, self.to)
        estado_global[self.to] = 'finalizado'

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
        return Response({"Desculpe, não consegui localizar seu endereço. O CEP deve estar no formato XXXXX-XXX."}, status=404)

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
        return Response({"Desculpe, não consegui localizar seu endereço. O CEP deve estar no formato XXXXX-XXX."}, status=404)

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

class EnviarMensagem(APIView):
    def post(self, request):
        body = request.data.get('body')  
        to = "whatsapp:+556293977594"   
        entrada = Entrada_de_menssagem(to)
        entrada.receber_mensagem(body)
        return Response({"status": "mensagem enviada"})