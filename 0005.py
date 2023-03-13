import math

num1, num2 = input().split()
num1, num2 = float(num1), float(num2)
# print(num1, num2)

inSquare = (num1 ** 2) + (num2 ** 2)
square = float(math.sqrt(inSquare))
print("{:.6f}".format(square))