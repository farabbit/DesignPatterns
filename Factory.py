# interface
class Car:
    def display(self):
        print(self.__class__)

# concrate class
class Audi(Car):
    pass

class Benz(Car):
    pass

# factory
class CarFactory:
    def productNewCar(self, brand):
        if brand == 'Audi':
            return Audi()
        elif brand == 'Benz':
            return Benz()

cf = CarFactory()
car_1 = cf.productNewCar("Benz").display() # car_1 will be seen as a Car