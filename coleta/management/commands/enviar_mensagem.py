import os
from django.core.management.base import BaseCommand
from coleta.views import enviar_mensagem

class Command(BaseCommand):
    help = 'Envia uma mensagem de teste usando a API do Twilio'

    def handle(self, *args, **kwargs):
        body = 'Bolha lobo gorro 020233982'
        to = 'whatsapp:+556293977594'
        message_sid = enviar_mensagem(body, to)
        self.stdout.write(self.style.SUCCESS(f'Mensagem enviada com sucesso! SID: {message_sid}'))