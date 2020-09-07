
import smtplib
import ssl
#system@menatee.net
# GetGlean3167*
port = 587  # For SSL
smtp_server = "mail.gandi.com"
sender_email = "system@menatee.net"  # Enter your address
receiver_email = "pk554115@gmail.com"  # Enter receiver address
password = "GetGlean3167*"
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()

with smtplib.SMTP('mail.gandi.net',587) as server: #smtplib.SMTP_SSl(smtp_server, port, context=context) as server:
    try:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        print('sended...')
    except Exception as e:
        print(e)
