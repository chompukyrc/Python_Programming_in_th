arr = []
for num in range(5):
    arr.append(list(map(int, input().split())))
# print(arr)

_max = 0
p_max = 0

for i in range(len(arr)):
    # print(i)
    temp = 0
    for ii in arr[i]:
        # print(ii)
        temp += ii
    if temp >= _max:
        _max = temp
        p_max = i+1

print(p_max, _max)
