import copy

class Prototype:
    def clone(self):
        # Uses deepcopy to clone itself
        return copy.deepcopy(self)

class Human(Prototype):
    def __init__(self):
        self.height = None 
        self.weight = None
        self.name = None 

    def setHeight(self, height):
        self.height = height

    def setWeight(self, weight):
        self.weight = weight

    def setName(self, name):
        self.name = name 

    def __str__(self):
        return f"Human with {self.name} name, {self.height} height, {self.weight} weight."


# Create the prototype
base_human = Human()
base_human.setHeight("5'11")
base_human.setWeight("80")
base_human.setName("John Doe")

print("Human:", base_human)

# Clone it and modify the clone
new_human = base_human.clone()
new_human.setName("Johnny English")
new_human.setWeight("100")

print("Clone:", new_human)
