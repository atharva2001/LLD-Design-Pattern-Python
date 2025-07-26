from abc import ABC, abstractmethod

class CarMaker(ABC):

    def build_car(self):
        self.add_wheels()
        self.add_interior()
        self.add_engine()
        self.add_nitros()

    def add_wheels(self):
        print("Adding 4 wheels...")

    def add_interior(self):
        print("Adding good interior...")

    @abstractmethod
    def add_engine(self):
        pass 

    def add_nitros(self):
        pass 


class Ferrari(CarMaker):
    
    def add_engine(self):
        print("Adding V12 Engine...")


class Supra(CarMaker):

    def add_engine(self):
        print("Adding V8 Engine...")

    def add_nitros(self):
        print("Adding NoS...")

print("\nFerrai:")
ferrari = Ferrari()
ferrari.build_car()
print("\nSupra")
supra = Supra()
supra.build_car()
