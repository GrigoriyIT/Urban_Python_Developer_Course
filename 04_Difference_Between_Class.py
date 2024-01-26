class Buiding:
    total = 0

    def __init__(self):
        Buiding.total += 1


listOfBuiding = []
while len(listOfBuiding) < 40:
    new_buiding = Buiding()
    listOfBuiding.append(new_buiding)
print(Buiding.total)