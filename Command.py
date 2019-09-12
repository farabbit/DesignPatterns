import abc

class Command:
    """ base command class """
    @abc.abstractmethod
    def execute(self): pass

class IncreaseCommand(Command):
    """ Concrete command classes traditional move """
    def __init__(self, receiver): self.receiver = receiver

    def execute(self): self.receiver.increase()

class DecreaseCommand(Command):
    """ Concrete command classes with functional programming """

    def __init__(self, receiver, times=1):
        self.receiver = receiver
        self.times = times

    # with __call__ implemented, DecreaseCommand became a function
    # which can save status during multiple function calls
    def __call__(self):
        for i in range(self.times):
            self.receiver.decrease()

class Receiver:
    def __init__(self, value): self.value=value

    def increase(self): self.value+=1; print(self.value)

    def decrease(self): self.value-=1; print(self.value)

class Invoker:
    def __init__(self): self.receiver=Receiver(0)

    # traditional move
    def increaseTimes(self, times):
        inC = IncreaseCommand(self.receiver)
        for i in range(times):
            inC.execute()
    
    # with functional programming
    def decreaseTimes(self, times):
        deC = DecreaseCommand(self.receiver, times)
        deC()

inv = Invoker()
inv.increaseTimes(7)
inv.decreaseTimes(5)
