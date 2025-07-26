from abc import ABC, abstractmethod

# Visitor Interface
class ShapeVisitor(ABC):
    @abstractmethod
    def visit_circle(self, circle):
        pass

    @abstractmethod
    def visit_rectangle(self, rectangle):
        pass

# Element Interface
class Shape(ABC):
    @abstractmethod
    def accept(self, visitor: ShapeVisitor):
        pass

# Concrete Elements
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def accept(self, visitor: ShapeVisitor):
        visitor.visit_circle(self)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def accept(self, visitor: ShapeVisitor):
        visitor.visit_rectangle(self)

# Concrete Visitor
class ExportVisitor(ShapeVisitor):
    def visit_circle(self, circle):
        print(f"Exporting Circle with radius {circle.radius}")

    def visit_rectangle(self, rectangle):
        print(f"Exporting Rectangle with width {rectangle.width} and height {rectangle.height}")

# Usage
shapes = [Circle(5), Rectangle(3, 4)]
exporter = ExportVisitor()

for shape in shapes:
    shape.accept(exporter)
