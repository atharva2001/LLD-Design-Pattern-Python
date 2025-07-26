class HumanType:
    def __init__(self, bones, teeth, gender):
        self.bones = bones 
        self.teeth = teeth
        self.gender = gender 

    def get_details(self, name, country):
        print(f"{name} with country {country} and bones {self.bones}, teeth {self.teeth}, gender {self.gender}")


class Humanfactory:
    _human_type = {} 

    @classmethod
    def get_human_type(cls, bones, teeth, gender):
        key = (bones, teeth, gender)
        if key not in cls._human_type:
            cls._human_type[key] = HumanType(bones, teeth, gender)
            print(f"Creating new Human Type {key}")

        return cls._human_type[key]
    

class Human:
    def __init__(self, name, country, human_type: HumanType):
        self.name = name
        self.country = country 
        self.human_type = human_type

    def get_details(self):
        self.human_type.get_details(self.name, self.country)


class Planet:
    def __init__(self):
        self.humans = []

    def create_humans(self, name, country, bones, teeth, gender):
        human_type = Humanfactory.get_human_type(bones, teeth, gender)
        human = Human(name, country, human_type)
        self.humans.append(human)

    def get_details(self):
        for humans in self.humans:
            humans.get_details()


earth = Planet()
earth.create_humans("John", "USA", "206", "32", "Male")
earth.create_humans("Ron", "Canada", "206", "32", "Male")
earth.create_humans("Jacob", "Australia", "206", "32", "Male")
earth.create_humans("Jasmine", "USA", "206", "32", "Female")
earth.create_humans("Daisy", "New Zealand", "206", "32", "Female")

print("\nHumans:")
earth.get_details()

    