inp = int(input())
result = []

for i in range(inp):
    temp = int(input())
    temp = pow(2, temp)
    result.append(temp)

for i in result:
    print(i)
