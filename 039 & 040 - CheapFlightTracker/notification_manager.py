import os
import smtplib
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")

my_email_address = os.getenv("my_email_address")
my_email_password = os.getenv("my_email_password")


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

    def send_emails(self, msg, emails):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()  # SECURITY ENCODING!
            connection.login(user=my_email_address, password=my_email_password)
            for email in emails:
                connection.sendmail(
                    from_addr=my_email_address,
                    to_addrs=email,
                    msg=f"Subject:🔺New Price Alert🔻\n\n{msg}".encode('utf-8')
                    )
