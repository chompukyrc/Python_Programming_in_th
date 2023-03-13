a = int(input())
b = int(input())
c = int(input())

if 0 <= a <= 30 and 0 <= b <= 30 and 0 <= b <= 40:
    score = a + b + c
    if 80 <= score <= 100:
        print("A")
    elif 75 <= score <= 79:
        print("B+")
    elif 70 <= score <= 74:
        print("B")
    elif 65 <= score <= 69:
        print("C+")
    elif 60 <= score <= 64:
        print("C")
    elif 55 <= score <= 59:
        print("D+")
    elif 50 <= score <= 54:
        print("D")
    elif 0 <= score <= 49:
        print("F")