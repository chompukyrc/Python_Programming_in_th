import math

jump, distance = map(int, input().split())

if jump > distance:

    print("2")
else:
    result = distance / jump
    print(math.ceil(result))
