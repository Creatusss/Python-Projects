class Animal:
    def speak(self):
        print("Sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
            print("Meow!")

class Cow(Animal):
        def speak(self):
            print("Moo!")

animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.speak()