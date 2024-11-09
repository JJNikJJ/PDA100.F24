from currency_api import get_exchange_rates
from currency_converter import convert


def main():
    # Получаем курсы валют
    exchange_rates = get_exchange_rates()
    # Проверяем, успешно ли получены курсы валют
    if not exchange_rates:
        return

    # Приветственное сообщение и доступные валюты
    print("Добро пожаловать в программу обмена валют!")
    print("Доступные валюты:", ", ".join(exchange_rates.keys()))

    # Запрашиваем у пользователя исходную и целевую валюты
    from_currency = input("Введите валюту, которую вы хотите обменять (например, RUB, USD): ").upper()
    to_currency = input("Введите валюту, которую вы хотите получить: ").upper()

    # Проверяем, чтобы пользователь не выбрал одинаковые валюты для обмена
    if from_currency == to_currency:
        print("Валюты совпадают. Обмен невозможен.")
        return

    # Запрашиваем сумму для конвертации и проверяем корректность ввода
    try:
        amount = float(input(f"Введите сумму в {from_currency}: "))
        if amount <= 0:
            print("Сумма должна быть больше нуля.")
            return
    except ValueError:
        print("Некорректный ввод суммы.")
        return

    # Конвертируем сумму с помощью функции convert
    converted_amount = convert(amount, from_currency, to_currency, exchange_rates)

    # Если конвертация успешна, выводим результат
    if converted_amount is not None:
        print(f"{amount} {from_currency} -> {converted_amount} {to_currency}")


if __name__ == "__main__":
    main()
