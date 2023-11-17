import math
perimeter = 0
x1 = float(input("Enter the x part of the coordinate: "))
y1 = float(input("Enter the y part of the coordinate: "))
x3 = x1
y3 = y1
x2 = input("Enter the x part of the coordinate (blank to quit): ")
while x2 != '':
    x = float(x2)
    y = float(input("Enter the y part of the coordinate: "))
    distance = math.sqrt((x3 - x) ** 2 + (y3 - y) ** 2)
    perimeter = perimeter + distance
    x3 = x
    y3 = y
    x2 = input("Enter the x part of the coordinate (blank to quit): ")
distance = math.sqrt((x1 - x) ** 2 + (y1 - y) ** 2)
perimeter = perimeter + distance
print("The perimeter of the polygon is:",perimeter)
