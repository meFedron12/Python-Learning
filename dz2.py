# Пусть у нас есть массив чисел numbers = [3, 5, 2, 6, 8].
# Нужно вывести сумму первого и последнего элементов массива.

mass = [3, 5, 2, 6, 8]
print(mass[0] + mass[4])


# # Пусть у нас есть массив слов pets = ["cat", "dog", "fish", "hamster", "parrot"].
# # Нужно вывести в консоль второе и четвертое слово через запятую.

words = ["cat", "dog", "fish", "hamster", "parrot"]
print(words[1] + ", " + words[-2])
print('-------------------------')

# задание 1

a = [10, 5, 3]
b = [10, 5, 3]
c = [10, 5, 3]
print(id(a), id(b), id(c))
print('-------------------------')

d = [1, 2, 3]
e = {1, 2, 3}
print(id(d), id(e))
print('-------------------------')


# задание 2

tuple_ = (1, 2, 3)
_, a, _ = tuple_
_, _, b = tuple_
c, _, _ = tuple_

print(a, b, c)
print('-------------------------')


# задание 3

countries_capitals = {
  'Belarus': 'Minsk',
  'Poland': 'Warsaw',
  'Great Britain': 'London',
}

print(countries_capitals['Poland'])
print(countries_capitals['Belarus'])
print('-------------------------')


# задание 4

food = ['котлета', 'пюрешка', 'драники', 'пиццу', 'мороженное']
print(f"больше всего я люблю {food[3]} и {food[4]}")
print('-------------------------')


# задание 5

name = input()

friends = ['Egor', 'Liza', 'Vanya', 'Yana']

if name in friends:
    print(f"У меня есть друг {name}")
else:
    print(f"У меня нет друга с именем {name}")

print('-------------------------')
