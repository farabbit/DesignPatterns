import abc

class Product: # interface
    def display(self):
        print(self.__class__)

class Product1(Product):
    pass

class Product2(Product):
    pass

class Factory: # interface
    @abc.abstractclassmethod
    def newProduct(cls):
        pass

class Product1Factory(Factory):
    @classmethod
    def newProduct(cls):
        return Product1()

class Product2Factory(Factory):
    @classmethod
    def newProduct(cls):
        return Product2

factoryType = "Product1Factory"
fac = globals()[factoryType]()

prod_1 = fac.newProduct()
prod_1.display()
