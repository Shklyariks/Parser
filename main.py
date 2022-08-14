from mailsender import send_mail
from parser import array
from record_results import create_post
from time import sleep
from support import menu, search, report

print('Программа по сбору естественного языка')
sleep(1)
menu()
while True:
    try:
        choice = int(input('Выберите нужный пункт меню: '))

        if choice == 1:
            create_post(array())
            break

        elif choice == 2:
            search()

        elif choice == 3:
            report()
            while True:
                send = input('Отправить ссылки на почту? (y/n):\n')
                if send == 'y':
                    send_mail(report())
                    break
                if send == 'n':
                    break
                else:
                    print('y или n')

        elif choice == 4:
            break
    except ValueError:
        print('Введите номер пункта меню')
