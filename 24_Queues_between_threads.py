import queue, threading, time


class Table:
    def __init__(self, number: int):
        self.number = number
        self.is_busy = False


class Cafe:
    def __init__(self, tables):
        self.queue = queue.Queue()
        self.tables = tables

    def customer_arrival(self):  # моделирует приход посетителя(каждую секунду).
        for customer_num in range(1, 21):
            customer = Customer(customer_num, None)
            print(f'Посетитель № {customer.number} прибыл')
            cafe.serve_customer(customer)
            time.sleep(1)

    def serve_customer(self, customer):  # Моделирует обслуживание в кафе
        i = 0
        while i < len(tables):
            if not tables[i].is_busy:
                customer.table_num = i
                customer.start()
                return
            i += 1

        self.queue.put(customer)
        print(f"Посетитель номер {customer.number} ожидает свободный стол.")

        while True:
            i = 0
            while i < len(tables):
                if not tables[i].is_busy:
                    customer = self.queue.get()
                    customer.table_num = i
                    customer.start()
                    return
                i += 1


class Customer(threading.Thread):
    def __init__(self, number, table_num, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.number = number
        self.table_num = table_num

    def run(self):
        tables[self.table_num].is_busy = True
        print(f"Посетитель номер {self.number} сел за стол {tables[self.table_num].number}.")
        time.sleep(5)
        print(f"Посетитель номер {self.number} покушал и ушёл.")
        tables[self.table_num].is_busy = False


# Создаем столики в кафе
table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

# Инициализируем кафе
cafe = Cafe(tables)

# Запускаем поток для прибытия посетителей
customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

# Ожидаем завершения работы прибытия посетителей
customer_arrival_thread.join()
