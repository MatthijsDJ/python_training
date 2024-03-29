import math
from typing import Self


class Circle:
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def get_radius(self) -> float:
        return self._radius

    def set_radius(self, radius: float) -> Self:
        if radius < 0.0:
            raise ValueError("Radius can't be negative.")
        else:
            self._radius = radius
            return self

    radius = property(get_radius, set_radius)

    @property
    def circumference(self):
        return 2.0 * math.pi * self._radius

    @circumference.setter
    def circumference(self, value):
        if value < 0.0:
            raise ValueError("Circumference can't be smaller than 0.0")
        else:
            self._radius = value / (2.0 * math.pi)

    @property
    def diameter(self):
        return self._radius * 2.0

    @diameter.setter
    def diameter(self, diameter):
        if diameter < 0.0:
            raise ValueError("Diameter can't be negative.")
        else:
            self._radius = diameter / 2.0

    def __str__(self) -> str:
        return f"Circle with radius {self.radius}."

    def __repr__(self):
        return f"Circle(radius={self.radius})"

    def __gt__(self, other):
        return self._radius > other.radius

    def __lt__(self, other):
        return self._radius < other.radius

if __name__ == "__main__":
    circle = Circle(radius=3.4)
    circle_2 = Circle(radius=4.5)
    print(circle)
    print("Radius", circle.radius)
    print("Circumference", circle.circumference)
    circle.circumference = 12.3
    print("Diameter", circle.diameter)
    try:
        circle.radius = -5.0  # ValueError
    except ValueError:
        print("Can't set the radius")