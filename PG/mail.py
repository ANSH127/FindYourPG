import requests
import smtplib 
from email.mime.text import MIMEText
from django.conf import settings 


def send_forget_password_mail(email,token):
    
    message = f'Hi ,click on the link to reset your password http://127.0.0.1:8000/change_password/{token}/'
     



    msg = MIMEText(message)
    msg['From'] = "eror86946@gmail.com"
    msg['To'] = email
    msg['Subject'] = "Reset Password"
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("eror86946@gmail.com", "myfoffzgizswcaha")
    server.send_message(msg,"eror86946@gmail.com",email)
    
    server.quit()
        
    return True
