import os
import smtplib
import ssl
from email.message import Message

from dotenv import load_dotenv

load_dotenv()

port = 465
smtp_server = os.getenv("SMTP_SERVER")
sender_email = os.getenv("EMAIL_SENDER")
password = os.getenv("EMAIL_PASSWORD")


def sendmail(receiver_email, subject, message_body):
	context = ssl.create_default_context()
	message = Message()
	message["Subject"] = subject
	message.add_header("Content-Type", "text/html")
	message.set_payload(message_body)

	with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
		server.login(sender_email, password)
		server.sendmail(sender_email, receiver_email, message.as_string().encode("utf-8"))
