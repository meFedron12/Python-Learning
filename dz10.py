from time import sleep


print("-------------------------")


class Auto:

    def __init__(self, brand, age, mark, weight=None, color=None):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    def move(self):
        print("move")

    def stop(self):
        print("stop")

    def birthday(self):
        self.age += 1


auto = Auto("BMW", 12, "E92")
auto.move()
auto.stop()
auto.birthday()
print(auto.age)

print("-------------------------")


class Truck(Auto):
    max_load = 4000

    def move_1(self):
        print("attention")
        super().move()

    def load(self):
        delay = 1
        sleep(delay)
        print("load")
        sleep(delay)


class Car(Auto):

    def speed(self, max_speed):
        super().move()
        print(f"max speed is {max_speed}")


auto_1 = Truck("BMW", 11, "E90")
auto_1.move_1()
auto_1.load()

auto_2 = Car("BMW", 13, "E91")
auto_2.birthday()
auto_2.speed(360)
print(auto_2.age)

print("-------------------------")

