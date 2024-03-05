import time
from threading import Thread


def outputs(data):
    for elem in data:
        time.sleep(1)
        print(elem)


i = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
c = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
t = Thread(target=outputs, kwargs=dict(data=i))
t.start()

outputs(c)
