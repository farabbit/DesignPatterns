# note: static class OR singleton or normal class ?
# in this example, every used handler is a static class

import abc

# Request: 
class Request:
    def __init__(self, value):
        self.value = value

    def display(self):
        print(self.value)

# base handler class, a handler is a kind of service that serves Request
class Handler: # abstract handler
    @abc.abstractclassmethod
    def filter(cls, requestObj):
        pass

    @abc.abstractclassmethod
    def handle(cls, requestObj):
        pass

class Handler1(Handler): # concrate handler 1
    @classmethod
    def filter(cls, requestObj):
        pass
        return True

    @classmethod
    def handle(cls, requestObj):
        if cls.filter(requestObj):
            requestObj.value += "\nHandled by handler 1"

class Handler2(Handler): # concrate handler 2
    @classmethod
    def filter(cls, requestObj):
        pass
        return True

    @classmethod
    def handle(cls, requestObj):
        if cls.filter(requestObj):
            requestObj.value += "\nHandled by handler 2"

 # this is one solution, another solution is use succesor chain inside every handler class
class HandlerChain:
    def __init__(self, requestObj):
        self.ChainOfResponsbility = [] # register chain
        self.requestObj = requestObj

    def register(self, Handler):
        self.ChainOfResponsbility.append(Handler)

    def start(self):
        for i in range(len(self.ChainOfResponsbility)):
            self.ChainOfResponsbility[i].handle(self.requestObj)


newRequestObj = Request("This is init message")
chain = HandlerChain(newRequestObj)

# regist service
chain.register(Handler1)
chain.register(Handler2)

# start & display
print("First handle result: ")
chain.start()
newRequestObj.display()

print("\nSecond handle result: ")
chain.start()
newRequestObj.display()
