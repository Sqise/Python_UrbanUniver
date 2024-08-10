# Есть система управления складом, где каждую минуту поступают запросы
# на обновление информации о поступлении товаров и отгрузке товаров.
# Задача заключается в разработке программы, которая будет эффективно
# обрабатывать эти запросы в многопользовательской среде, с использованием механизма
# мультипроцессорности для обеспечения быстрой реакции на поступающие данные.


import multiprocessing
from typing import Dict, Tuple


# Создайте класс WarehouseManager - менеджера склада, который будет обладать следующими свойствами:
# 1. Атрибут data - словарь (изначально пустой), где ключ - название продукта, а значение - его количество.
class WarehouseManager:
    def __init__(self):
        self.data: Dict[str, int] = {}
        self.lock = multiprocessing.Lock()

    # 2. Метод process_request - реализует запрос (действие с товаром), принимая request - кортеж.
    def process_request(self, request: Tuple[str, str, int]):
        action, product, quantity = request

        # Есть 2 действия: receipt - получение, shipment - отгрузка.
        with self.lock:
            # а) В случае получения данные должны поступить в data
            # (добавить пару, если её не было и изменить значение ключа, если позиция уже была в словаре)
            if action == 'receipt':
                if product in self.data:
                    self.data[product] += quantity
                else:
                    self.data[product] = quantity
                print(f"Получено: {quantity} единиц товара '{product}'. Текущий запас: {self.data[product]}")

            # б) В случае отгрузки данные товара должны уменьшаться
            # (если товар есть в data и если товара больше чем 0).
            elif action == 'shipment':
                if product in self.data and self.data[product] > 0:
                    if self.data[product] >= quantity:
                        self.data[product] -= quantity
                        print(f"Отгружено: {quantity} единиц товара '{product}'. Текущий запас: {self.data[product]}")
                    else:
                        print(f"Недостаточно товара '{product}' для отгрузки. Запас: {self.data[product]}")
                else:
                    print(f"Товар '{product}' отсутствует на складе")

    # 3. Метод run - принимает запросы и создаёт для каждого свой
    # параллельный процесс, запускает его (start) и замораживает (join).
    def run(self, requests: list):
        processes = []
        for request in requests:
            process = multiprocessing.Process(target=self.process_request, args=(request,))
            processes.append(process)
            process.start()

        for process in processes:
            process.join()


if __name__ == "__main__":
    manager = WarehouseManager()
    requests = [
        ('receipt', 'apple', 10),
        ('receipt', 'banana', 5),
        ('shipment', 'apple', 3),
        ('shipment', 'banana', 2),
        ('shipment', 'orange', 1),  # Товар отсутствует
        ('shipment', 'apple', 10),  # Недостаточно товара
        ('receipt', 'banana', 10),
        ('shipment', 'banana', 5)
    ]

    manager.run(requests)
