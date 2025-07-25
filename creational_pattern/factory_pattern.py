class Burger:
    def __init__(self, ing):
        self.ing = ing

    def __str__(self):
        return f"{self.ing}"
    

class BurgerFactory:
    def cheeseBurger(self):
        ing = ["bread", "cheese", "lettuce"]
        return Burger(ing) 
    
    def chickenBurger(self):
        ing = ["bread", "chicken", "lettuce"]
        return Burger(ing)
    
    def fishBurger(self):
        ing = ["bread", "fish", "lettuce"]
        return Burger(ing)

  
burgerfactory = BurgerFactory()
print(burgerfactory.fishBurger())
    

