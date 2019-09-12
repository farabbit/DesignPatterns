import abc
import types


class Context:
    """ class that using Strategy """
    def __init__(self, intA, intB):
        self.intA, self.intB = intA, intB

    def setStrategy(self, strategy):
        self.strategy = strategy

    def executeStrategy(self):
        """ execute in difference cases """
        if isinstance(self.strategy, Strategy):
            # when strategy is a class
            return self.strategy.operation(self)
        else:
            # when strategy is a function
            return self.strategy(self)


""" Strategy pattern 1. Traditional way """
# every strategy is as class that inherits base stategy

class Strategy:
    """ Base Strategy """
    @abc.abstractmethod
    def operation(self, context): pass

# concrate stategies
class StrategyAdd(Strategy):
    def operation(self, context): return context.intA + context.intB
class StrategyMultiple(Strategy):
    def operation(self, context): return context.intA * context.intB


""" Strategy pattern 2. Restruct using functional programming """
# concrete stragegies had no internal status -> performanced like functions

# strategy functions
def StrategyMinus(context): return context.intA - context.intB

def StrategyDevide(context): return context.intA / context.intB

context = Context(6, 3)

context.setStrategy(StrategyAdd()) # using add
print("ADD:", context.executeStrategy()) # ADD: 9
context.setStrategy(StrategyMultiple()) # using multiple
print("MUL:", context.executeStrategy()) # MUL: 18

context.setStrategy(StrategyMinus) # using minus
print("Minus:", context.executeStrategy()) # ADD: 3
context.setStrategy(StrategyDevide) # using devide
print("Devide:", context.executeStrategy()) # MUL: 2.0


""" 1. Find best strategy """
# additional functionalities
print("Choose best strategy among all: ")

strategies = [StrategyMinus,StrategyDevide]

def bestStrategy(context):
    """ choose a best strategy from strategy list """
    return max(strategy(context) for strategy in strategies)

print("MAX(MIN(6,3),DEV(6,3)):", bestStrategy(Context(6,3))) # 6


""" 2. Find all strategies """
# using globals(): returns every global variable that in current module (module that defines that function/method)

strategies = [globals()[name] for name in globals()  if name.startswith('Strategy') and isinstance(globals()[name], types.FunctionType)]
print(strategies) # [StrategyMinus,StrategyDevide]
print(bestStrategy(context))

""" 3. use decorator to enhance strategy registory """
# using decorator to regist every strategy, no need to add them to the list manually

strategies = []
def registe(StrategyFunc):
    strategies.append(StrategyFunc)
    return StrategyFunc

@registe
def StrategyPower(context): return context.intA ^ context.intB

@registe
def StrategyRoot(context): return context.intA * context.intB
print(strategies) # [<function StrategyPower at 0x0000023F04B869D8>, <function StrategyRoot at 0x0000023F04B86AE8>]
print(bestStrategy(context)) # bestStrategy is still available because it depends on the list

"""out: 
ADD: 9
MUL: 18
Minus: 3
Devide: 2.0
Choose best strategy among all:
MAX(MIN(6,3),DEV(6,3)): 3
[<function StrategyMinus at 0x0000021EBE8CCD08>, <function StrategyDevide at 0x0000021EBE9668C8>]
3
[<function StrategyPower at 0x0000021EBE9669D8>, <function StrategyRoot at 0x0000021EBE966AE8>]
18
"""