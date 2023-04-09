# 1. Написать бесконечный итератор, который возвращает случайно число в заданном диапазоне.
# Реализовать через класс-итератор и через функцию-генератор.
# Протестировать обе реализации в цикле for.

# Дополнительно (если есть время) добавить параметр стоп-число: как только генератор
# выдает стоп-число, он заканчивает генерировать новые.

import random


print("---------------------------")


class Randomize:

    def __init__(self, first_num=None, second_num=None, stop_iteration_num=None):
        self.first_num = first_num
        self.second_num = second_num
        self.stop_iteration_num = stop_iteration_num

    def __next__(self):
        result = random.randint(self.first_num, self.second_num)
        if result == self.stop_iteration_num:
            raise StopIteration
        return result

    def __iter__(self):
        return self


random_int = Randomize(20, 30, 25)

for num in random_int:
    print(num)


print("---------------------------")


def randomize(first_num: int, second_num: int, stop_num: int = None):
    while True:
        result = random.randint(first_num, second_num)
        if stop_num == result:
            break
        yield result
    return result


random_int_2 = randomize(10, 18, 15)

for num in random_int_2:
    print(num)


print("---------------------------")