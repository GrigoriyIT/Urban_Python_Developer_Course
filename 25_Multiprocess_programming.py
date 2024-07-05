import multiprocessing as mp


class WarehouseManager:
    def __init__(self):
        self.data = {}

    def process_request(self, request):
        name, action, kolvo = request
        if action == 'shipment':
            if self.data.get(name) is not None and self.data[name] >= kolvo:
                self.data[name] -= kolvo
        if action == 'receipt':
            if self.data.get(name) is not None:
                self.data[name] += kolvo
            else:
                self.data[name] = kolvo

    def run(self, requests):
        # # НЕ многопоточно
        # for i in requests:
        #     self.process_request(i)

        # Многопоточно вар 1
        for request in requests:
            process = mp.Process(target=self.process_request, args=(request, ))
            process.start()
            process.join()

        # Многопоточно вар 2
        # with mp.Pool() as pool:
        #     pool.map(self.process_request, requests)

if __name__ == '__main__':

    # Создаем менеджера склада
    manager = WarehouseManager()

    # Множество запросов на изменение данных о складских запасах
    requests = [
        ('product1', 'receipt', 100),
        ('product2', 'receipt', 150),
        ('product1', 'shipment', 30),
        ('product3', 'receipt', 200),
        ('product2', 'shipment', 50)
    ]

    # Запускаем обработку запросов
    manager.run(requests)

    # Выводим обновленные данные о складских запасах
    print(manager.data)
