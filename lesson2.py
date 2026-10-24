import random

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.skill = 1
        self.money = 1000

    def study(self):
        self.skill += 1
        self.money -= 50
        print("Studying... -50 грн")

    def chill(self):
        self.skill -= 0.5
        self.money -= 40
        print("Chilling... -40 грн")

    def work(self):
        self.money += 250
        print("Working... +250 грн")

    def info(self):
        print(f"My name is {self.name}. Im {self.age} years old")
        print(f"Skills: {self.skill} Great!")
        print(f"Money: {self.money} грн")

alex = Student("Alex", 15)
alex.info()

for day in range(366):
    choice = random.randint(0, 2)

    if choice == 0:
        alex.chill()
    elif choice == 1:
        alex.study()
    else:
        alex.work()

alex.age += 1
alex.info()