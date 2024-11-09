# Функция для конвертации суммы из одной валюты в другую
def convert(amount, from_currency, to_currency, exchange_rates):
    # Проверяем, есть ли введённые валюты в словаре курсов
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        print("Ошибка: неверная валюта")
        return None

    # Конвертируем сумму в рубли
    rub_amount = amount * exchange_rates[from_currency]
    converted_amount = rub_amount / exchange_rates[to_currency]
    return round(converted_amount, 2)
