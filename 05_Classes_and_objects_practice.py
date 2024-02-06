from random import randint
from termcolor import cprint


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'я - {}, сытость {}'.format(
            self.name, self.fullness)

    def work(self):
        print('{} ходил на работу'.format(self.name))
        self.house.money += 50
        self.fullness -= 10

    def eat(self):
        if self.house.food >= 10:
            print('{} поел'.format(self.name))
            self.fullness += 10
            self.house.food -= 10
        else:
            print('{} нет еды'.format(self.name))

    def watch_MTV(self):
        print('{} Смотрел МТВ целый день'.format(self.name))
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            print('{} сходил в магазин за едой'.format(self.name))
            self.house.money -= 50
            self.house.food += 50
        else:
            print('у {} деньги закончились'.format(self.name))

    def go_into_house(self, house):
        self.house = house
        print('{} въехал в дом!!!'.format(self.name))
        self.fullness -= 10

    def act(self):
        if self.fullness <= 0:
            print('{} умер...'.format(self.name))
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_MTV()


class House:
    def __init__(self):
        self.food = 50
        self.money = 50

    def __str__(self):
        return 'в доме еды {}, денег {}'.format(
            self.food, self.money)


citizens = [
    Man('Бивис'),
    Man('Батхед'),
    Man('Кенни')
]

my_sweet_home = House()
for citizen in citizens:
    citizen.go_into_house(my_sweet_home)

for day in range(1, 366):
    print('====== день {} ======'.format(day))
    for citizen in citizens:
        citizen.act()
    print('------ в конце дня ------')
    for citizen in citizens:
        print(citizen)
    print(my_sweet_home)
