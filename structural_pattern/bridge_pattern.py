class Color:
    def fill(self):
        pass 

class Red(Color):
    def fill(self):
        return ("Shape filled with Red Color")

class Blue(Color):
    def fill(self):
        return ("Shape filled with Blue Color")


class Shape:
    def __init__(self, color: Color):
        self.color = color

    def draw(self):
        pass 

class Circle(Shape):
    def draw(self):
        return f"Circle {self.color.fill()}"
    

class Square(Shape):
    def draw(self):
        return f"Square {self.color.fill()}"
    

red = Red()
blue = Blue()


red_circle = Circle(red)
blue_square = Square(blue)

print(red_circle.draw())
print(blue_square.draw())