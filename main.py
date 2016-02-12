import math


def circle(radius):
    return radius * math.pi * 2


r = float(input("Enter the radius please:"))
x = circle(r)
print(x)
