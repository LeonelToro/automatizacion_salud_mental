# enviar_mail.py
import os
import smtplib
from email.message import EmailMessage

def enviar_mail_con_adjuntos(gmail_user, gmail_app_password, to_email, output_dir,
                             subject='Análisis Salud Mental - Envío automático',
                             body='Envío análisis del formulario de pedidos de atención de salud mental'):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = gmail_user
    msg['To'] = to_email
    msg.set_content(body)

    for filename in os.listdir(output_dir):
        filepath = os.path.join(output_dir, filename)
        if os.path.isfile(filepath):
            with open(filepath, 'rb') as f:
                file_data = f.read()
                file_name = os.path.basename(filepath)

            if filename.lower().endswith('.xlsx'):
                maintype, subtype = 'application', 'vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            elif filename.lower().endswith('.png'):
                maintype, subtype = 'image', 'png'
            elif filename.lower().endswith(('.jpg', '.jpeg')):
                maintype, subtype = 'image', 'jpeg'
            elif filename.lower().endswith('.docx'):
                maintype, subtype = 'application', 'vnd.openxmlformats-officedocument.wordprocessingml.document'
            elif filename.lower().endswith('.txt'):
                maintype, subtype = 'text', 'plain'
            else:
                maintype, subtype = 'application', 'octet-stream'

            msg.add_attachment(file_data, maintype=maintype, subtype=subtype, filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(gmail_user, gmail_app_password)
        smtp.send_message(msg)
    print(f"Correo enviado a {to_email}")
