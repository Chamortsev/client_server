"""
Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах. Написать скрипт,
автоматизирующий его заполнение данными. Для этого:
Создать функцию write_order_to_json(), в которую передается 5 параметров
— товар (item), количество (quantity), цена (price), покупатель (buyer), дата (date).
Функция должна предусматривать запись данных в виде словаря в файл orders.json.
При записи данных указать величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
"""
import json


def write_order_to_json(item, quantity, price, buyer, date):
    with open('orders.json', encoding='utf-8') as f:
        my_orders = json.load(f)
        order = {
            "item": item,
            "quantify": quantity,
            "price": price,
            "buyer": buyer,
            "date": date,
                 }

        my_orders['orders'].append(order)
    with open('orders.json', 'w', encoding='utf-8') as f:
        json.dump(my_orders, f, indent=4)


write_order_to_json('Куртка', 2, 3500, 'Армен Николаевич', '2022-02-09')
write_order_to_json('Футболка', 3, 990, 'Армен Николаевич', '2022-02-09')
write_order_to_json('Брюки', 1, 1990, 'Армен Николаевич', '2022-02-09')
write_order_to_json('Костюм', 5, 13500.50, 'Армен Николаевич', '2022-02-10')
