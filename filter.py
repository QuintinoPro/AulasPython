
valores = [10, 20, 30, 40, 50]


def remove(x):
    return x>20

print(list(filter(remove, valores)))

print(list(filter(lambda x: x>20, valores)))