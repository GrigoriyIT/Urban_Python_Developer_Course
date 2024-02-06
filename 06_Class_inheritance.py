class Car:
    price = 1000000

    def horse_powers(self):
        self.horse_powers = 100
        return self.horse_powers

    def __str__(self):
        return '{} - {} - {}'.format(
            self.__class__.__name__, self.horse_powers(), self.price)


class Nissan(Car):
    price = 1500000

    def horse_powers(self):
        self.horse_powers = 150
        return self.horse_powers


class Kia(Car):
    price = 2000000

    def horse_powers(self):
        self.horse_powers = 200
        return self.horse_powers


nissan = Nissan()
kia = Kia()

print(nissan)
print(kia)
