num = list(map(int, input().split()))
pos = list(input())

num.sort()

result = [0, 0, 0]
result[pos.index("A")] = num[0]
result[pos.index("B")] = num[1]
result[pos.index("C")] = num[2]

print(*result)