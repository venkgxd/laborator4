import requests


def get_exchange_rate():
    url = "https://v6.exchangerate-api.com/v6/7357db211277051e0b9f791b/latest/USD"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        rate_usd_to_rub = data['conversion_rates']['RUB']
        rate_rub_to_usd = 1 / rate_usd_to_rub
        return rate_usd_to_rub, rate_rub_to_usd
    else:
        print("Ошибка при получении данных.")
        return None, None


def convert_currency(amount, rate):
    return amount * rate


def main():
    print("Конвертер валют (Рубли и Доллары)")

    rate_usd_to_rub, rate_rub_to_usd = get_exchange_rate()

    if rate_usd_to_rub and rate_rub_to_usd:
        while True:
            print("\n1. Конвертировать рубли в доллары")
            print("2. Конвертировать доллары в рубли")
            print("3. Выход")
            choice = input("Выберите действие (1/2/3): ")

            if choice == '1':
                rubles = float(input("Введите сумму в рублях: "))
                dollars = convert_currency(rubles, rate_rub_to_usd)
                print(f"{rubles} рубля(ей) = {dollars:.2f} долларов США по курсу {rate_rub_to_usd:.2f} руб./долл.")

            elif choice == '2':
                dollars = float(input("Введите сумму в долларах: "))
                rubles = convert_currency(dollars, rate_usd_to_rub)
                print(f"{dollars} доллар(ов) = {rubles:.2f} рублей по курсу {rate_usd_to_rub:.2f} долл./руб.")

            elif choice == '3':
                print("Выход из программы...")
                break

            else:
                print("Неверный выбор, попробуйте снова.")
    else:
        print("Не удалось получить курс валют.")


if __name__ == "__main__":
    main()
