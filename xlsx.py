import xlsxwriter

from Project.main import array

#Импортируем библиотеку по работе с Excel

def writer(parametr):

    # Объявляем функцию writer и передаем в нее параметр

    book = xlsxwriter.Workbook(r'/Users/sergejsklarik/PycharmProjects/banki.xlsx')
    # Создаем таблицу с именем data
    page = book.add_worksheet('Item')
    # Создаем страницу Excel с названием Item

    row = 0
    column = 0
    # Устанавливаем ширину колонок
    page.set_column('A:A', 20)
    page.set_column('B:B', 20)
    page.set_column('C:C', 50)
    page.set_column('D:D', 50)
    page.set_column('E:E', 50)
    page.set_column('F:F', 50)


    for item in parametr:
        # Итерируем полученные данные
        # Записываем данные в row - строку и column - столбец. От 0 до бесконечности
        page.write(row, column, item[0])
        page.write(row, column + 1, item[1])
        page.write(row, column + 2, item[2])
        page.write(row, column + 3, item[3])
        page.write(row, column + 4, item[4])
        page.write(row, column + 5, item[5])
        row += 1
    book.close()


writer(array())
