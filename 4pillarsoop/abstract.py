class Car:
    def start(self):
        self.__ignite_engine()
        print("Car Started")

    def __ignite_engine(self):
        print("Engine Ignited Successfully")

car1 = Car()
car1.start()