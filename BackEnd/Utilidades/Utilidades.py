#email
from http import HTTPStatus
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

from django.http import JsonResponse
from dotenv import load_dotenv

def SendMail (html, asunto, destino) :
    mensaje =MIMEMultipart('alternative')
    mensaje['Subject'] = asunto
    mensaje['From'] =  os.getenv('3fd44e4d9627c3')
    mensaje['To'] = destino
    
    mensaje.attach(MIMEText(html, 'html'))
    
    try :
        server = smtplib.SMTP('sandbox.smtp.mailtrap.io', '587')
        server.login('0709f9d0c4f25e', '1c0da43b781b2c')
        server.sendmail('3fd44e4d9627c3', destino, mensaje.as_string())
        server.quit()
    except smtplib.SMTPResponseException as e:
        return JsonResponse ({"Estado" : "Error", "Mensaje" : "Error al enviar el correo"}, status = HTTPStatus.BAD_REQUEST)
    
#ESTE METODO ES SIEMPRE ASI, LO QUE CAMBIA SON LAS CREDENCIALES OSEA USUARIO Y CONTRASEÑA, EL PUERTO Y LA URL, QUE DEPENDE DEL SERVIDOR Y DEMAS