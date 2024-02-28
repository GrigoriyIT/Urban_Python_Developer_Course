class EvenNumbers:
    def __init__(self, start=0, end=1):
        self.start = start
        self.end = end
        self.i = 0
        self.result = self.start

    def __iter__(self):
        self.i = 0
        self.result = self.start
        return self

    def __next__(self):
        self.result = self.start + self.i
        if self.result > self.end:
            raise StopIteration
        if self.result % 2:
            self.i += 1
            self.result = self.start + self.i
            if self.result > self.end:
                raise StopIteration
        self.i += 1
        return self.result


en = EvenNumbers(10, 25)
for i in en:
    print(i)
