
#МОДУЛЬ 3
#Программа "Личный счет"


def amaunt():
    total_amount = 0
    purchase_history = []
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')
        print((f' Ваш баланс {total_amount}'))

        choice = input('Выберите пункт меню  ')
        if choice == '1':
            balance_account = int(input('Введите сумму  '))
            total_amount += balance_account
        elif choice == '2':
            amount_purchases = int(input('Введите сумму покупки  '))
            if amount_purchases > total_amount:
                print('Недостатчно средств на счете')
            else:
                total_amount -= amount_purchases
                purchase_name = input('Введите название покупки  ')
                purchase_history.append((purchase_name, amount_purchases))
        elif choice == '3':
            print('Список покупок: ', purchase_history)
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')

