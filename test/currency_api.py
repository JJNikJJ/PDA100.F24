import requests
from xml.etree import ElementTree as ET


# Функция для получения актуальных курсов валют с сайта ЦБ РФ
def get_exchange_rates():
    url = "https://www.cbr.ru/scripts/XML_daily.asp"
    response = requests.get(url)  # Отправляем запрос к API

    # Проверяем успешность запроса
    if response.status_code != 200:
        print("Ошибка при запросе данных от ЦБ РФ")
        return None

    exchange_rates = {}  # Словарь для хранения курсов валют
    tree = ET.fromstring(response.text)  # Парсим XML-ответ от ЦБ РФ

    # Проходимся по каждой валюте в XML-дереве
    for valute in tree.findall("Valute"):
        code = valute.find("CharCode").text  # Код валюты
        rate = float(valute.find("Value").text.replace(",", "."))  # Курс валюты
        nominal = int(valute.find("Nominal").text)  # Номинал валюты
        exchange_rates[code] = rate / nominal  # Рассчитываем курс для 1 единицы валюты

    exchange_rates["RUB"] = 1.0  # Добавляем курс рубля (1 RUB = 1 RUB)
    return exchange_rates  # Возвращаем словарь курсов
