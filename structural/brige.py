"""
The Bridge pattern decouples an abstraction from its implementation, allowing both to vary independently.

Key Points:
- Purpose: Decouple abstraction from implementation.
- Use case: Useful when both the abstraction and implementation may evolve independently.
"""


class DrawingAPI:
    def draw_circle(self, x, y, radius):
        raise NotImplementedError


class DrawingAPI1(DrawingAPI):
    def draw_circle(self, x, y, radius):
        return f"API1.circle at ({x},{y}) with radius {radius}"


class DrawingAPI2(DrawingAPI):
    def draw_circle(self, x, y, radius):
        return f"API2.circle at ({x},{y}) with radius {radius}"


class Circle:
    def __init__(self, x, y, radius, drawing_api):
        self.x = x
        self.y = y
        self.radius = radius
        self.drawing_api = drawing_api

    def draw(self):
        return self.drawing_api.draw_circle(self.x, self.y, self.radius)


# Usage
circle1 = Circle(1, 2, 3, DrawingAPI1())
circle2 = Circle(4, 5, 6, DrawingAPI2())

print(circle1.draw())  # Output: API1.circle at (1,2) with radius 3
print(circle2.draw())  # Output: API2.circle at (4,5) with radius 6
