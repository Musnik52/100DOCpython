import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")


class NotificationManager:
    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_msg(self, msg):
        message = self.client.messages.create(
            body=msg,
            from_="+12014688388",
            to=os.getenv("my_phone_number"),
        )
        print(message.status)
