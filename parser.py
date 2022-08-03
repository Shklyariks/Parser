import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from time import sleep

ua = UserAgent()
headers = {'User-Agent': ua.random}
'''print(ua.chrome)'''
'''headers = {'UserAgent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) '
               'Chrome/41.0.2228.0 Safari/537.36'}'''


def get_url():

    for count in range(1, 2):
        sleep(3)
        url = f'https://www.banki.ru/insurance/responses/company/vsk/?page={count}/'
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        data = soup.find_all('article', class_='responses__item')
        for i in data:
            card_url = 'https://www.banki.ru' + i.find('a').get('href')
            yield card_url


def array():

    for card_url in get_url():
        response = requests.get(card_url, headers=headers)
        sleep(3)
        soup = BeautifulSoup(response.text, 'html.parser')
        data = soup.find('div', class_='layout-wrapper padding-top-default bg-white position-relative')
        header = data.find('h1', class_='header-h0').string
        grade = data.find('span', {'data-test': 'responses-rating-grade'})
        if grade is None:
            grade = 'Nonetype'
        else:
            grade = grade.get_text()
        status = data.find('span', {'data-test': 'responses-status'})
        if status is None:
            status = 'Nonetype'
        else:
            status = status.string
        timeb = data.find('time', itemprop='dtreviewed').string
        city = data.find('div', class_='color-gray-burn').string
        message = data.find('div', class_='article-text response-page__text markup-inside-small markup-inside-small--bullet').text
        yield header, timeb, status, city, message, card_url

