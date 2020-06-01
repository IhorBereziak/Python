# Написати програму, яка підраховує вартість витрачених коштів за тиждень.
#   1)Ви записуєте: дату, товар і ціну,
#   2)ці записи можна редагувати,
#   3)таких записів у вас може бути безліч
#   4)у вас має бути меню:
#     - список всіх записів
#     - загальна вартість всіх покупок
#     - найдорожча покупка
#     - пошук по назві товару
#     - покупки по днях
notebook = [
    {'date': 2, 'purchases': [
        {'product': 'Orange', 'price': 60},
    ]},
    {'date': 3, 'purchases': [
        {'product': 'Milk', 'price': 50},
        {'product': 'Car', 'price': 200000},
    ]},
    {'date': 4, 'purchases': [
        {'product': 'Cabbage', 'price': 15},
        {'product': 'Carrot', 'price': 30},
        {'product': 'Potato', 'price': 10},
    ]},
    {'date': 1, 'purchases': [
        {'product': 'Fridge', 'price': 4500},
    ]},
    {'date': 5, 'purchases': [
        {'product': 'Beef', 'price': 180},
        {'product': 'Wine', 'price': 220},
    ]}
]

def hr():
    print('------------------------------------------------------')

def show_purchases(purchases):
    for purchase in purchases:
        print(f"Product: {purchase.get('product')}, Price: {purchase.get('price')}")

def is_empty(nbook):
    if not len(nbook):
        hr()
        print('Notebook is empty')
        hr()
        return True

def get_all(nbook):
    if is_empty(nbook):
        return
    for item in nbook:
        hr()
        date = item.get('date')
        print(f"Date: {date}:")
        show_purchases(item.get('purchases'))
        hr()

def sum_all_costs(nbook):
    if is_empty(nbook):
        return
    hr()
    print("Sum of all purchases is:", sum(purchase.get('price') for item in nbook for purchase in item.get('purchases')))
    hr()
    # l = []
    # for item in nbook:
    #     for purchase in item.get('purchases'):
    #         l.append(purchase.get('cost'))

def most_expensive(nbook):
    if is_empty(nbook):
        return
    max_price = max(purchase.get('price') for item in nbook for purchase in item.get('purchases'))
    hr()
    for item in nbook:
        for purchase in item.get('purchases'):
            if max_price == purchase.get('price'):
                print(
                    f"The most expensive purchase is {purchase.get('product')}, price: {max_price}, date: {item.get('date')}")
    hr()

def find_by_product(nbook, name):
    if is_empty(nbook):
        return
    hr()
    check = True
    for item in nbook:
        for purchase in item.get('purchases'):
            if name.lower().strip() == purchase.get('product').lower().strip():
                print(f"Date {item.get('date')}, {name.title()}, price: {purchase.get('price')}")
                check = False
    if check:
        print("Product not found!!!")
    hr()

def show_by_day(nbook, day):
    if is_empty(nbook):
        return
    hr()
    for item in nbook:
        if day == str(item.get('date')):
            print(f"Date {day}:")
            show_purchases(item.get('purchases'))
            hr()
            return
    print("Date not found!!!")
    hr()

# show_by_day(notebook, '2')
# find_by_product(notebook, 'tie')
# most_expensive(notebook)
# sum_all_costs(notebook)
# get_all(notebook)

while True:
    print('1. Показати всі покупки')
    print('2. Загальна вартість всіх покупок')
    print('3. Показати найбільш дорогу покупку')
    print('4. Пошук по назві товару')
    print('5. Показати покупки по днях')
    print('6. Вихід')
    choice = input('Зробіть свій вибір: ')
    print('')
    if not choice.isdigit():
        continue
    choice = int(choice)
    if choice == 1:
        get_all(notebook)
    if choice == 2:
        sum_all_costs(notebook)
    if choice == 3:
        most_expensive(notebook)
    if choice == 4:
        find_by_product(notebook, input("Enter product name: "))
    if choice == 5:
        show_by_day(notebook, input("Enter day: "))

    if choice == 6:
        break