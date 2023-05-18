inp = int(input())
result = []

for i in range(inp):
    temp = int(input())
    if temp == 2:
        result.append("T")
    elif temp % 2 != 0:
        result.append("T")
    else:
        result.append("F")

for i in result:
    print(i)
