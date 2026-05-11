class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} is making a sound...")

class Dog(Animal):
    pass

class Cat(Animal):
    pass

class Bird(Animal):
    pass

dog1 = Dog('Chuchu')
dog1.sound()

cat1 = Cat("Miming")
cat1.sound()

bird1 = Bird("Twitwi")
bird1.sound()