inp = list(input())
# print(inp)

posBall = 0

for i in inp:
    if i == "A" and posBall != 2:
        posBall = 0 if posBall == 1 else 1
    elif i == "B" and posBall != 0:
        posBall = 1 if posBall == 2 else 2
    elif i == "C" and posBall != 1:
        posBall = 2 if posBall == 0 else 0
print(posBall + 1)