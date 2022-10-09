import smtplib
import mimetypes
from email.message import EmailMessage 

class Mail:

    def __init__(self):
        self.port = 465
        self.smtp_server_domain_name = "smtp.gmail.com"
        self.sender_mail = "christina.12mar@gmail.com"
        self.password = ""


    def send(self, logs):
        message = EmailMessage()
        message['From'] = self.sender_mail
        message['To'] = self.sender_mail
        message['Subject'] = 'Logs'
        body = """Hi from logger"""
        message.set_content(body)
        mime_type, _ = mimetypes.guess_type(logs)
        mime_type, mime_subtype = mime_type.split('/')
        with open(logs,'rb') as file:
            message.add_attachment(file.read(),
            maintype=mime_type,
            subtype=mime_subtype,
            filename=logs)
        print(message)

        mail_server = smtplib.SMTP_SSL(self.smtp_server_domain_name, self.port)
        mail_server.login(self.sender_mail, self.password)
        mail_server.send_message(message)
        mail_server.quit()

if __name__ == '__main__':
    logs = input()
    mail = Mail()
    mail.send(logs)
