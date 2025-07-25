from __future__ import annotations
from abc import ABC, abstractmethod

class HondaFactory(ABC):

    @abstractmethod
    def createCar(self) -> Car:
        pass

    @abstractmethod
    def createBike(self) -> Bike:
        pass
    

class IndiaFactory(HondaFactory):

    def createCar(self) -> Car:
        return IndianCar()

    def createBike(self) -> Bike:
        return IndianBike()

class USFactory(HondaFactory):
    
    def createCar(self) -> Car:
        return USCar()

    def createBike(self) -> Bike:
        return USBike()
    

class Car(ABC):

    @abstractmethod
    def definition(self) -> str:
        pass


class IndianCar(Car):

    def definition(self) -> str:
        return "This is an Indian Honda Car."
    
class USCar(Car):
    
    def definition(self) -> str:
        return "This is a US Honda Car."
    

class Bike(ABC):

    @abstractmethod
    def definition(self) -> str:
        pass

    @abstractmethod
    def collaboration_car(self, car: Car) -> str:
        pass

class IndianBike(Bike):

    def definition(self) -> str:
        return "This is an Indian Honda Bike."
    
    def collaboration_car(self, car: Car) -> str:
        return f"Collaboration with {car.definition()}"
    
class USBike(Bike):

    def definition(self) -> str:
        return "This is a US Honda Bike."
    
    def collaboration_car(self, car: Car) -> str:
        return f"Collaboration with {car.definition()}"
    



def main(factory: HondaFactory):
    car = factory.createCar()
    bike = factory.createBike()
    
    print(f"Car: {car.definition()}")
    print(f"Bike: {bike.definition()} collaboration: {bike.collaboration_car(car)}")


if __name__ == "__main__":
    india_factory = IndiaFactory()
    us_factory = USFactory()
    
    print("Using India Factory:")
    main(india_factory)
    
    print("\nUsing US Factory:")
    main(us_factory)
    



