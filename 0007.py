import math

rad = int(input())

# เรขาคณิตทั่วไป
num1 =  math.pi * (rad ** 2)

# เรขาคณิต Taxi
num2 = 2 * (rad ** 2)

print("{:.6f}".format(num1))
print("{:.6f}".format(num2))