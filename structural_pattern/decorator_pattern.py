from abc import ABC, abstractmethod

class Coffee(ABC):
    
    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def description(self):
        pass 


class BasicCoffee(Coffee):

    def cost(self):
        return 5
    
    def description(self):
        return "Simple Coffee"
    
class CoffeeDecorator(Coffee):

    def __init__(self, coffee: Coffee):
        self._coffee = coffee

    @abstractmethod
    def cost(self):
        pass 

    @abstractmethod
    def description(self):
        pass

class MilkDecorator(CoffeeDecorator):

    def cost(self):
        return self._coffee.cost() + 2
    
    def description(self):
        return self._coffee.description() + ", Milk"
    
class SugarDecorator(CoffeeDecorator):

    def cost(self):
        return self._coffee.cost() + 1
    
    def description(self):
        return self._coffee.description() + ", Sugar"
    


simple = BasicCoffee()
print(f"{simple.description()} : ${simple.cost()}")

# Add Milk
milk_coffee = MilkDecorator(simple)
print(f"{milk_coffee.description()} : ${milk_coffee.cost()}")

# Add Milk + Sugar
milk_sugar_coffee = SugarDecorator(milk_coffee)
print(f"{milk_sugar_coffee.description()} : ${milk_sugar_coffee.cost()}")
    
