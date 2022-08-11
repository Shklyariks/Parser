import smtplib

import openpyxl


def send_mail(message):
    sender = 'Shklyarik.s.a@inbox.ru'
    # password = 'razuEw'
    password = 'QuYBVhAmz1AcRXfCcaCi'

    server = smtplib.SMTP('smtp.mail.ru', 587)
    server.starttls()

    try:
        server.login(sender, password)
        server.sendmail(sender, 'Shklyarik.s.a@gmail.com', message)
        return print('Sended')
    except Exception as ex:
        return f'{ex} ERROR'

def report():
    book = openpyxl.load_workbook('Banki.ru.xlsx')
    sheet = book.active.values
    message_list = []
    for i in sheet:
        if i[3] == '05.08.2022':
            message_list.append(i)
        print(message_list)
    message = ' '.join(message_list)
    return message
send_mail(report())
