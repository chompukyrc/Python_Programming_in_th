# inp = list(map(int, input().split()))
# print(inp)

inp = []
for i in range(0, 10):
    inp.append(int(input()))

arr = [0]*42

for i in inp:
    arr[i%42] = 1

print(sum(arr))
