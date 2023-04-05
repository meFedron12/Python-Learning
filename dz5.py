# 1


def chet_nechet(num: int) -> bool:
    if type(num) != int:
        print("Введенные данные не являются числом")
    else:
        otvet = bool(num % 2 == 0)
    return otvet


print(chet_nechet(4))


# 2


n = int(input())

for x in range(n):
    if chet_nechet(x):
        print(x**2)
    elif x % 7 == 0 and x % 4 == 0:
        break

