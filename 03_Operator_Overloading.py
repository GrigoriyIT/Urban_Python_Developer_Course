class Buiding:
    def __init__(self, floors: int, buildType: str):
        self.numberOfFloors = floors
        self.buildingType = buildType

    def __eq__(self, other):
        if self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType:
            return 'дома одинаковые'
        else:
            return 'дома разные'


home_1 = Buiding(floors=10, buildType='home')
home_2 = Buiding(floors=10, buildType='town')

print(home_1 == home_2)
