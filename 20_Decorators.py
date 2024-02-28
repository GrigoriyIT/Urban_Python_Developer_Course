def is_prime(func):
    def surrogate(*args, **kwargs):
        result = func(*args, **kwargs)
        counter = 0
        for i in range(1, result + 1):
            if result % i == 0:
                counter += 1
        print('Простое число' if counter == 2 else 'Составное число')
        return result

    return surrogate


@is_prime
def sum_three(a, b, c):
    sum = a + b + c
    return sum


print(sum_three(2, 3, 6))
