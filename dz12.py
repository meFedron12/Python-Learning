# 1
from datetime import datetime
import random


print("---------------------------")


class func_time:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        if args and kwargs:
            print(f"Функция {self.func.__name__} вызвана в {datetime.now()} с позиционными {args} и "
                  f"именнованными параметрами {kwargs}")
        elif kwargs:
            print(f"Функция {self.func.__name__} вызвана в {datetime.now()} с именнованными параметрами {kwargs}")
        elif args:
            print(f"Функция {self.func.__name__} вызвана в {datetime.now()} с позиционными параметрами {args}")
        else:
            print(f"Функция {self.func.__name__} вызвана в {datetime.now()} без параметров")
        return result


@func_time
def chet(a=0, b=0):
    return a + b


func_time_1 = func_time(chet)
chet(a=1, b=3)
chet(1, b=3)
chet(1, 3)
chet()

print("---------------------------")

# 2.1

print(f"Если хочешь выбрать камень, напиши 1 \n"
      f"Если хочешь выбрать ножницы, напиши 2 \n"
      f"Если хочешь выбрать бумагу, напиши 3")

c = random.randint(1, 3)

try:
    game_1 = int(input())

    if c == 1:
        print("Бот выбрал камень:")
    if c == 2:
        print("Бот выбрал ножницы:")
    if c == 3:
        print("Бот выбрал бумагу:")

    if c == 1 and game_1 == 3:
        print("Поздравляю ты победил")
    if c == 1 and game_1 == 1:
        print("Похоже у нас ничья, сыграем еще раз ?")
    if c == 1 and game_1 == 2:
        print("Увы, ты проиграл")

    if c == 2 and game_1 == 1:
        print("Поздравляю ты победил")
    if c == 2 and game_1 == 2:
        print("Похоже у нас ничья, сыграем еще раз ?")
    if c == 2 and game_1 == 3:
        print("Увы, ты проиграл")

    if c == 3 and game_1 == 2:
        print("Поздравляю ты победил")
    if c == 3 and game_1 == 3:
        print("Похоже у нас ничья, сыграем еще раз ?")
    if c == 3 and game_1 == 1:
        print("Увы, ты проиграл")
except (NameError, ValueError):
    print("Вы ввели не число")


print("---------------------------")

# 2.2


def step(num):
    try:
        for x in range(num):
            if x == 0:
                print(x)
            elif x % 7 == 0 and x % 4 == 0:
                break
            elif x % 2 == 0:
                print(x ** 2)
            else:
                print(x)
    except TypeError:
        print("Вы ввели не число")
    return


print(step(["bsjcbwjzsbc"]))
print(step(10))

print("---------------------------")
