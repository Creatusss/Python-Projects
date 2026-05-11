class Car:
    def __init__(self, color, brand, speed):
        self.color = color
        self.brand = brand
        self.speed = speed

    def start(self):
        print(f"The {self.brand} is now starting...")

    def stop(self):
        print(f"The {self.brand} is now stopping...")

    def accelerate(self, amount):
        self.speed += amount
        print(f"The {self.brand} is now {self.speed}")

    def info(self):
        print(f"Brand: {self.brand} | Color: {self.color} | Speed: {self.speed} ")



car1 = Car("Red", "Toyota", 100)
car2 = Car("Blue", "Honda", 80)
car3 = Car("White", "Mitsubishi", 90)

cars = [car1, car2, car3]
for car in cars:
    car.start()
    car.accelerate(20)
    car.stop()
    car.info()

