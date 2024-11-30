from twilio.rest import Client
import os
from pathlib import Path
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

def envio_mensagem( mensagem):
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=mensagem,  # Altere para a mensagem que deseja enviar
        to= "whatsapp:+556293977594"

    )

    return message.sid
