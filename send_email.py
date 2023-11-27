import os
import smtplib, ssl
from dotenv import load_dotenv

load_dotenv()

host = "smtp.gmail.com"
port = 465

username = os.environ['USERNAME']
password = os.environ['PASSWORD']


context = ssl.create_default_context()

message = """\
Subject: Hello World
How are you?
dude
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, username, message)