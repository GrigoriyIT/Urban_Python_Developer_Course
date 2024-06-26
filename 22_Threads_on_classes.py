import time
from threading import Thread


class Knight(Thread):
    def __init__(self, name, skill, *args, **kwargs):
        super(Knight, self).__init__(*args, **kwargs)
        self.name = name
        self.skill = skill

    def run(self):
        enemys = 100
        days = 0
        print(f'{self.name}, на нас напали!')
        while enemys != 0:
            time.sleep(1)
            days += 1
            enemys -= self.skill
            print(f'{self.name}, сражается {days} день(дня)..., осталось {enemys} воинов.')
        print(f'{self.name} одержал победу спустя {days} дней!')


knight1 = Knight("Sir Lancelot", 10)  # Низкий уровень умения
knight2 = Knight("Sir Galahad", 20)  # Высокий уровень умения
knight1.start()
knight2.start()
knight1.join()
knight2.join()
print('Все битвы закончились!')