import threading
import time
from queue import Queue


class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False


class Customer(threading.Thread):
    def __init__(self, id, cafe):
        super().__init__()
        self.id = id
        self.cafe = cafe

    def run(self):
        self.cafe.serve_customer(self)


class Cafe:
    def __init__(self, tables):
        self.queue = Queue()
        self.tables = tables
        self.lock = threading.Lock()

    def customer_arrival(self):
        customer_id = 1
        while customer_id <= 10:  # 10 посетителей
            print(f"Посетитель № {customer_id} прибыл.")
            customer = Customer(customer_id, self)
            customer.start()  # Запуск потока для нового посетител
            customer_id += 1
            time.sleep(1)  # Новые посетители приходят каждую секунду

    def serve_customer(self, customer):
        with self.lock:
            free_table = self.find_free_table()
            if free_table:
                # Если есть свободный стол
                free_table.is_busy = True
                print(f"Посетитель № {customer.id} сел за стол {free_table.number}. (= начало обслуживания)")
                # Обслуживание в отдельном потоке
                threading.Thread(target=self.customer_service, args=(customer, free_table)).start()
            else:
                # Если нет свободного стола, помещаем в очередь
                print(f"Посетитель № {customer.id} ожидает свободный стол (= в очереди).")
                self.queue.put(customer)

    def find_free_table(self):
        for table in self.tables:
            if not table.is_busy:
                return table
        return None

    def customer_service(self, customer, table):
        time.sleep(5)  # Время обслуживания 5 секунд
        print(f"Посетитель № {customer.id} поел и ушёл. (= конец обслуживания)")
        self.finish_service(table)

        # Проверка очереди на наличие ожидающих клиентов
        self.check_queue()

    def finish_service(self, table):
        with self.lock:
            table.is_busy = False

    def check_queue(self):
        while not self.queue.empty():
            customer = self.queue.get()
            free_table = self.find_free_table()
            if free_table:
                free_table.is_busy = True
                print(f"Посетитель № {customer.id} сел за стол {free_table.number}. (= начало обслуживания)")
                threading.Thread(target=self.customer_service, args=(customer, free_table)).start()
            else:
                # Если нет свободного стола, клиент возвращается в очередь
                self.queue.put(customer)
                break


# 3 стола
tables = [Table(i) for i in range(1, 4)]

# Кафе со столами
cafe = Cafe(tables)

# Поток для прихода посетителей
threading.Thread(target=cafe.customer_arrival).start()
