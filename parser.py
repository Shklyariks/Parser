import openpyxl
import requests
from bs4 import BeautifulSoup
from time import sleep
import re

headers = {'UserAgent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/41.0.2228.0 Safari/537.36'}


def get_url():
    url_main = 'https://www.banki.ru/insurance/responses/company/vsk/'
    response_main = requests.get(url_main, headers=headers)
    soup_main = BeautifulSoup(response_main.text, 'lxml')
    data_main = soup_main.find('div', class_='ui-pagination__description').text
    page = [i for i in data_main.split()]
    page = page[-1]
    page = int(page)
    #for count in range(1, page):
    for count in range(1, 2):
        # Идем постранично
        try:
            sleep(3)
            url = f'https://www.banki.ru/insurance/responses/company/vsk/?page={count}/'
            response = requests.get(url, headers=headers)
            print(f'Код {response.status_code}: Соединение установлено')
            soup = BeautifulSoup(response.text, 'lxml')
            data = soup.find_all('article', class_='responses__item')
            for i in data:
                card_url = 'https://www.banki.ru' + i.find('a').get('href')
                yield card_url
        except ConnectionError:
            print('Соединение отсутствует')


def array():
    for card_url in get_url():

        book = openpyxl.load_workbook('Banki.ru.xlsx')
        sheet = book.active.values
        allredyin = []

        for i in sheet:
            if str(i[0]) == card_url:
                allredyin.append(i[0])
                #print(i[0])
                #print('Данные уже были записаны')
                break
            print(f'{len(allredyin)} элементов уже записаны')
        else:
            response = requests.get(card_url, headers=headers)
            sleep(3)
            soup = BeautifulSoup(response.text, 'html.parser')
            data = soup.find('div', class_='layout-wrapper padding-top-default bg-white position-relative')
            header = data.find('h1', class_='header-h0').string
            grade = data.find('span', class_="rating-grade")
            if grade is None:
                grade = 'Nonetype'
            else:
                grade = ' '.join(re.findall('\d', grade.string))

            status = data.find('span', {'data-test': 'responses-status'})
            # status = data.find('span', class_='text-label')
            if status is None:
                status = 'Нет статуса'
            else:
                status = ' '.join(re.findall('[\s\S]*', status.text))

            timeb = data.find('time', itemprop='dtreviewed').string
            city = data.find('div', class_='color-gray-burn')
            if city is None:
                city = 'Не указан'
            else:
                city = re.search('[гГ].\s?[А-Я][а-я]*([\s\S][А-Я][а-я]*)?', city.text).group(0)
            message = data.find('div',
                                class_='article-text response-page__text markup-inside-small markup-inside-small--bullet').text
            user = data.find('span',
                             class_="link-with-icon__text color-gray-blue--alpha-60 padding-right-xx-small").text
            yield card_url, user, header, timeb, grade, status, city, message
            print(f'Запись страницы: {card_url}')

