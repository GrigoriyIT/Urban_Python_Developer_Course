class House:
    def __init__(self):
        self.numberOfFloors = 10


house_01 = House()

house_01.currentFloor = 1
while house_01.currentFloor <= house_01.numberOfFloors:
    print(house_01.currentFloor)
    house_01.currentFloor += 1
