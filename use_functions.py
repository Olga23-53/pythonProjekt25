# Пример кода на Python
balance = 0  # Текущий баланс пользователя
purchase_history = []  # Список для хранения истории покупок


def main_menu():
    while True:
        print(f"\nВаш баланс: {balance} руб.\n")
        print("Выберите действие: ")
        print("1. Пополнить счет")
        print("2. Покупка")
        print("3. История покупок")
        print("4. Выход")

        choice = input("\nВведите номер действия: ")

        if choice == "1":
            deposit()
        elif choice == "2":
            buy()
        elif choice == "3":
            show_history()
        elif choice == "4":
            print("Выход из программы. До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


def deposit():
    global balance
    try:
        amount = float(input("Введите сумму пополнения: "))
        if amount > 0:
            balance += amount
            print(f"Баланс успешно пополнен. Текущий баланс: {balance} руб.")
        else:
            print("Сумма пополнения должна быть положительной.")
    except ValueError:
        print("Пожалуйста, введите корректное число.")


def buy():
    global balance
    global purchase_history

    if balance <= 0:
        print("Баланс = 0. Пополните счет.")
        return

    item = input("Введите название покупки: ")
    try:
        price = float(input("Введите стоимость покупки: "))
        if price <= balance:
            balance -= price
            purchase_history.append((item, price))  # Записываем покупку в историю
            print(f"Вы купили {item} за {price} руб. Текущий баланс: {balance} руб.")
        else:
            print("Недостаточно средств. Пополните счет")
    except ValueError:
        print("Пожалуйста, введите корректную стоимость.")


def show_history():
    if purchase_history:
        print("\nИстория покупок:")
        for i, (item, price) in enumerate(purchase_history, 1):
            print(f"{i}. {item} — {price} руб.")
    else:
        print("История покупок пуста.")  # Если история пуста


# Запуск программы
main_menu()
