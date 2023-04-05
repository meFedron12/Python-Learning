# 1

chet_nechet = lambda x: "четное" if x % 2 == 0 else "нечетное"

print(chet_nechet(2))


# 2

int_lst_ = [1, 2, 3, 4, 5, 6]

print(list(map(lambda num: str(num), int_lst_)))


# 3

tupl_ = ("анна", "егор", "филипп", "шалаш", "тащат")

print(tuple(filter(lambda word: word == word[-1::-1], tupl_)))


# 4

import time


def summa_decorator(func):
    def time_(*args):
        time_1 = time.time()
        result = func(*args)
        time_2 = time.time()
        print(f"Время ваыполнения функции: {time_2 - time_1}")
        return result
    return time_


@summa_decorator
def raznost(a, b):
    num = a - b
    print(f"Разность чисел: {num}")
    return num


@summa_decorator
def summa_(a, b):
    num = a + b
    print(f"Сумма чисел: {num}")
    return num


raznost(2, 4)
summa_(2, 4)


# 5

def analis_numbers(num: str):
    if num.isdigit():
        num = int(num)
        print(f"Вы ввели положительное целое число {num}")
    else:
        # if num[0] == ".":
        #     new_num = "0" + num[0:]
        #     if "." and "-" in num:
        #         str_3 = new_num.replace("-", "0")
        #         str_4 = str_3.replace(".", "0")
        #         if str_4.isdigit():
        #             new_num = float(new_num)
        #             print(f"Вы ввели отрицательное дробное число {new_num}")
        #         else:
        #             print(f"Вы ввели некорректное число {new_num}")
        #     elif "-" in new_num:
        #         str_1 = num.replace("-", "0")
        #         if str_1.isdigit():
        #             new_num = int(new_num)
        #             print(f"Вы ввели целое отрицательное число {new_num} ")
        #         else:
        #             print(f"Вы ввели некорректное число {new_num}")
        #     elif "." in new_num:
        #         str_2 = new_num.replace(".", "0")
        #         if str_2.isdigit():
        #             print(f"Вы ввели положительное дробное число {new_num}")
        #         else:
        #             print(f"Вы ввели некорректное число {new_num}")
        if "." and "-" in num:
            str_3 = num.replace("-", "0")
            str_4 = str_3.replace(".", "0")
            if str_4.isdigit():
                num = float(num)
                print(f"Вы ввели отрицательное дробное число {num}")
            else:
                print(f"Вы ввели некорректное число {num}")
        elif "-" in num:
            # if num[1] == ".":
            #     new_num = num[0] + "0" + num[1:]
            str_1 = num.replace("-", "0")
            if str_1.isdigit():
                num = int(num)
                print(f"Вы ввели целое отрицательное число {num} ")
            else:
                print(f"Вы ввели некорректное число {num}")
            str_1 = num.replace("-", "0")
            if str_1.isdigit():
                num = int(num)
                print(f"Вы ввели целое отрицательное число {num} ")
            else:
                print(f"Вы ввели некорректное число {num}")
        elif "." in num:
            str_2 = num.replace(".", "0")
            if str_2.isdigit():
                print(f"Вы ввели положительное дробное число {num}")
            else:
                print(f"Вы ввели некорректное число {num}")
        return num


analis_numbers("-563653")


