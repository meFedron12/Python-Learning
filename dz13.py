# 1. Написать бесконечный итератор, который возвращает случайно число в заданном диапазоне.
# Реализовать через класс-итератор и через функцию-генератор.
# Протестировать обе реализации в цикле for.

# Дополнительно (если есть время) добавить параметр стоп-число: как только генератор
# выдает стоп-число, он заканчивает генерировать новые.

import random


print("---------------------------")


class Randomize:

    def __init__(self, start_num: int, first_num=None, second_num=None, stop_iteration_num=None):
        self.start_num = start_num
        self.first_num = first_num
        self.second_num = second_num
        self.stop_iteration_num = stop_iteration_num

    def __next__(self):
        if self.stop_iteration_num is not None and self.start_num > self.stop_iteration_num:
            raise StopIteration
        result = random.randint(self.first_num, self.second_num)
        self.start_num += 1
        return result

    def __iter__(self):
        return self


random_int = Randomize(20, 30, 40, 25)

for num in random_int:
    print(num)


print("---------------------------")


def randomize(Start_num, first_num: int = None, second_num: int = None, Stop_num: int = None):
    while True:
        if Stop_num is not None and Start_num > Stop_num:
            break
        yield Start_num
        Start_num += 1
        print(random.randint(first_num, second_num))


random_int_2 = randomize(10, 20, 30, 15)

for num in random_int_2:
    pass


print("---------------------------")