import openpyxl
import datetime
book = openpyxl.load_workbook('Banki.ru.xlsx')
sheet = book.active.values
message_list = []
for i in sheet:
    message_list.append(i[3])
    for ditem in message_list:
        date = str(ditem).replace(' ', '')
        date = datetime.datetime.strptime(ditem, ' %d.%m.%Y %H:%M')
        print(date)
        # if date <= datetime.datetime.now() >= date:
        #     print(date)

