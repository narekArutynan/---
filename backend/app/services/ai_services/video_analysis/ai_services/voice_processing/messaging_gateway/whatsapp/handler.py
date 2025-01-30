from twilio.rest import Client
import os

class WhatsAppHandler:
    def __init__(self):
        self.client = Client(os.getenv('TWILIO_SID'), os.getenv('TWILIO_TOKEN'))

    def send_message(self, to: str, message: str):
        self.client.messages.create(
            body=message,
            from_='whatsapp:' + os.getenv('TWILIO_NUMBER'),
            to='whatsapp:' + to
        )
