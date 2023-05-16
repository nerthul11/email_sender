import os
import smtplib
from email.message import EmailMessage
import random

user_gmail = os.getenv('USER_GMAIL')
password_gmail = os.getenv('PASSWORD_GMAIL')
targets = []

def send_notifying_mail(mail_user: str = "", mail_password: str = "", targets: tuple = ()) -> None:
    # Definir contenido
    msg = EmailMessage()
    msg['From'] = mail_user
    msg['To'] = targets
    msg['Subject'] = "Tu ID ha sido generado!"


    id = ""
    chars = "0123456789abcdef"
    for c in range(8):
      id += random.choice(chars)
    id += "-"
    for i in range(3):
      for i in range(4):
        id += random.choice(chars)
      id += "-"
    for i in range(12):
      id += random.choice(chars)
    
    # Agregar al cuerpo del mensaje
    msg.set_content(f"Tu ID para ingresar a Falopa Inc es {id}")

    # Conectar a Gmail
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(mail_user, mail_password)

    # Enviar y desconectar
    server.send_message(msg)
    server.quit();

send_notifying_mail(user_gmail, password_gmail, ())
