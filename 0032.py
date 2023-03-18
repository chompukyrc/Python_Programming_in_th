inp = int(input())

arr = (list(map(int, input().split())))
arr.sort()

i = 1

while arr[0] == 0:
    arr[0], arr[i] = arr[i], arr[0]
    i += 1

result = ''.join([str(num) for num in arr])
print(result)
