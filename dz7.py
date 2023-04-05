from datetime import datetime
from functools import wraps


def count_time(func):
    @wraps(func)
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        if args and kwargs:
            print(f"Функция {func.__name__} вызвана в {datetime.now()} с позиционными {args} и "
                  f"именнованными параметрами {kwargs}")
        elif kwargs:
            print(f"Функция {func.__name__} вызвана в {datetime.now()} с именнованными параметрами {kwargs}")
        elif args:
            print(f"Функция {func.__name__} вызвана в {datetime.now()} с позиционными параметрами {args}")
        else:
            print(f"Функция {func.__name__} вызвана в {datetime.now()} без параметров")
        return result
    return inner


@count_time
def chet(*args):
    otvet = sum(args)
    print(otvet)
    return otvet


chet(1, 2)
chet(a=1, b=3)
chet(1, b=3)
chet()
