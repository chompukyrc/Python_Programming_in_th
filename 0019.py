inp = int(input())
arr = []

for num in range(inp):
    arr.append(list(map(int, input().split())))
    # print(arr)

_min = 1000000000

for i in range(1, 2**inp):
    b = bin(i)[2:].zfill(inp)
    sour = 1
    bitter = 0
    # print(b)
    for ii in range(len(b)):

        if b[ii] == "1":
            sour *= arr[ii][0]
            bitter += arr[ii][1]
            
    if abs(sour - bitter) < _min:
        _min = abs(sour - bitter)
    # print(b, sour, bitter, abs(sour - bitter))

print(_min)