class Transformers:
    def __init__(self):
        self.name = None 
        self.group = None
        self.intention = None

    def setName(self, name):
        self.name = name

    def setGroup(self, group):
        self.group = group

    def setIntention(self, intention):
        self.intention = intention

    def __str__(self) -> str:
        return (f"Transformer: {self.name}, Group: {self.group}, Intention: {self.intention}")

class AutobotBuilder:
    def __init__(self):
        self.transformer = Transformers()

    def addName(self, name):
        self.transformer.setName(name)
        return self
    
    def addGroup(self, group):
        self.transformer.setGroup(group)
        return self
    
    def addIntention(self, intention):
        self.transformer.setIntention(intention)
        return self
    
    def build(self):
        return self.transformer

class DecepticonBuilder:
    def __init__(self):
        self.transformer = Transformers()

    def addName(self, name):
        self.transformer.setName(name)
        return self
    
    def addGroup(self, group):
        self.transformer.setGroup(group)
        return self
    
    def addIntention(self, intention):
        self.transformer.setIntention(intention)
        return self
    
    def build(self):
        return self.transformer    

optimus_prime = AutobotBuilder()\
    .addName("Optimus Prime")\
    .addGroup("Autobot")\
    .addIntention("Protect humanity")\
    .build()

megatron = DecepticonBuilder()\
    .addName("Megatron")\
    .addGroup("Decepticon")\
    .addIntention("Conquer the universe")\
    .build()

print(optimus_prime)
print(megatron)