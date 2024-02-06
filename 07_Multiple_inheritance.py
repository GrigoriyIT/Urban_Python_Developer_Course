class Vehicle:
    vehicle_type = 'none'

class Car:
    price = 1000000

    def horse_powers(self):
        self.horse_powers = 100
        return self.horse_powers

class Nissan(Car, Vehicle):
    price = 5000000
    vehicle_type = 'Машина'

    def horse_powers(self):
        self.horse_powers = 250
        return self.horse_powers


nissan = Nissan()

print(nissan.vehicle_type)
print(nissan.price)
