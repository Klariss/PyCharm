import math

QUIT = 15749


# circle perimeter
def circle(radius):
    return radius * math.pi * 2


# circle area
def circle_area(radius):
    return radius ** 2 * math.pi


# rectangle perimeter
def rectangle_perimeter(side_a, side_b):
    return 2 * (side_a + side_b)


# rectangle area
def rectangle_area(side_a, side_b):
    return side_a * side_b


# square perimeter
def square_perimeter(side):
    return side * 4


# square area
def square_area(side):
    return side ** 2

