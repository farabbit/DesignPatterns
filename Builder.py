import abc

class Car:
    def display(self): # all properties are build by carBuilder
        print("Wheel " + self.Wheel)
        print("Frame " + self.Frame)

class CarBuilder: # builder interface
    @classmethod
    def build(cls, car): # *** can also put this method to Director
        cls.buildWheel(car)
        cls.buildFrame(car)
        return car

    @abc.abstractclassmethod
    def buildWheel(cls, car):
        pass
    
    @abc.abstractclassmethod
    def buildFrame(cls, car):
        pass

class AudiBuilder(CarBuilder): # concrete builder
    @classmethod
    def buildWheel(cls, car):
        car.Wheel = "AudiWheel"

    @abc.abstractclassmethod
    def buildFrame(cls, car):
        car.Frame = "AudiFrame"

class BenzBuilder(CarBuilder):
    @classmethod
    def buildWheel(cls, car):
        car.Wheel = "BenzWheel"

    @abc.abstractclassmethod
    def buildFrame(cls, car):
        car.Frame = "BenzFrame"

class Director:
    @classmethod
    # user tell Director which car to build by using carBuilder parameter
    def getCar(cls, carBuilder): # carBuilder = Builder interface
        car = Car() # new car

        return carBuilder.build(car)

car1 = Director.getCar(BenzBuilder)
car1.display()
