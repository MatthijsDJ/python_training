import math
from typing_extensions import Self


class Circle:
    def __init__(self, radius: float) -> None:
        self.radius = radius


    def get_radius(self) -> float:
        return self._radius
    
    def set_radius(self, radius):
        print('Using radius setter')
        
        if radius <= 0.0:
            raise ValueError('Radius can\'t be zero or negative')
        else:
            self._radius = radius
            return self
    
    def get_circumference(self) -> float:
        return math.pi * 2 * self._radius

    def set_circumference(self, radius) -> Self:
        self._circumference = math.pi * 2 * radius
        return self

    def get_diameter(self) -> float:
        return self._radius / 2.0

    def set_diameter(self, radius) -> Self:
        self._diameter = radius * 2.0
        return self


    radius = property(get_radius, set_radius)
    circumference = property(get_circumference, set_circumference)
    diameter = property(get_diameter, set_diameter)

if __name__ == '__main__':
    circle = Circle(radius=3.4)
    print(circle.get_circumference())
    circle2 = Circle(radius=7.5)
    print(circle2.circumference)
    print(circle2.diameter)
    circle3 = Circle(radius=-1)
    # print(f'Radius: {circle.radius}')
    # print(f'Circumference: {circle.circumference}')
    # circle.circumference = 12.3
    # print(f'Diameter: {circle.diameter}')
    # try:
    #     circle.radius = -5.0
    # except ValueError:
    #     print("Can's set the radius")