# 1
# Написать программу, которая получает имя и возраст пользователя, проверяет, что возраст 18 лет и старше
# и выдает приветсвенное сообщение в зависимости от возраста. Примеры работы:
# Имя Иван, возраст 34 -> "Приветсвую, Иван! У вас есть доступ к взрослому контенту."
# Имя Лиза, возраст 15 -> "Приветсвую, Лиза! У вас нет доступа к взрослому контенту."
# Имя Артем, возраст 18 -> "Приветсвую, Артем! Поздравляю с совершеннолетием! У вас нет доступа к взрослому контенту."


name = input()
age = int(input())

if age > 18:
    print(f"Здарова {name} тебе уже можно пить пиво")
elif age == 18:
    print(f"Здарова {name} в этом году тебе исполнилось 18, а значит ты уже можешь пить пиво")
else:
    print(f"Здарова {name} тебе пока нет 18, а значит ты пока не можешь пить пиво")


# 2*
# Пользователь вводит две строки. Нужно вывести True, если в обеих строках использовались одинаковые символы,
# и False иначе. Постараться решить, не используя циклы.
# Примеры работы:
# "abc" и "bca" -> True
# "aabc" и "abc" -> True
# "Abc" и "abc" -> False
# "abc" и "aaa" -> False

str_1 = input()
str_2 = input()


a = set(str_1)
b = set(str_2)

if a == b:
    print(True)
else:
    print(False)


# 3*
# Написать мини-игру «Камень ножницы бумага с ботом», в которой пользователь должен выбрать либо камень,
# либо ножницы, либо бумагу. Бот делает случайный выбор (случайное число).
# Вывести результат если, например, игрок выбрал бумагу, а бот ножницы:
# Бот выбрал ножницы, вы проиграли!
# Подсказка: я не показывала, как в Pyhon получить случайное число, попробуйте найти это сами


import random

game_converting = input()

c = random.randint(1, 3)

# 1 - камень
# 2 - ножницы
# 3 - бумага

game_converting_1 = game_converting.lower()
game_1 = game_converting_1.strip()

if c == 1:
    print("Бот выбрал камень, а значит:")
if c == 2:
    print("Бот выбрал ножницы, а значит:")
if c == 3:
    print("Бот выбрал бумагу, а значит:")


if c == 1 and "бумага" == game_1:
    print("Поздравляю ты победил")
if c == 1 and "камень" == game_1:
    print("Похоже у нас ничья, сыграем еще раз ?")
if c == 1 and "ножницы" == game_1:
    print("Увы, ты проиграл")


if c == 2 and "камень" == game_1:
    print("Поздравляю ты победил")
if c == 2 and "ножницы" == game_1:
    print("Похоже у нас ничья, сыграем еще раз ?")
if c == 2 and "бумага" == game_1:
    print("Увы, ты проиграл")


if c == 3 and "ножницы" == game_1:
    print("Поздравляю ты победил")
if c == 3 and "бумага" == game_1:
    print("Похоже у нас ничья, сыграем еще раз ?")
if c == 3 and "камень" == game_1:
    print("Увы, ты проиграл")


