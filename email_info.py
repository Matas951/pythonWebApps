import ssl, smtplib
import os



def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    context = ssl.create_default_context()

    username = "asmatas02@gmail.com"
    password = os.getenv("PASSWORD")
    # password = "usnellxvefloqoxh"

    receiver = "asmatas02@gmail.com"

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
