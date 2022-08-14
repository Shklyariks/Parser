import smtplib
import datetime
import openpyxl
from passwords import password_mail
from email.mime.text import MIMEText

def send_mail(message):
    sender = 'Shklyarik.s.a@inbox.ru'
    password = password_mail

    server = smtplib.SMTP('smtp.mail.ru', 587)
    server.starttls()

    try:
        server.login(sender, password)
        msg = MIMEText(message)
        msg['Subject'] = 'New update'
        server.sendmail(sender, 'Shklyarik.s.a@gmail.com', msg.as_string())
        return print('Sended')
    except Exception as ex:
        return f'{ex} ERROR'

def report():
    book = openpyxl.load_workbook('Banki.ru.xlsx')
    sheet = book.active.values
    message_list = []
    past = datetime.datetime.now() - datetime.timedelta(days=7)

    for i in sheet:
        date = datetime.datetime.strptime(i[3], ' %d.%m.%Y %H:%M')
        if date >= past:
            message_list.append(i[0])

    return ' '.join(message_list)

