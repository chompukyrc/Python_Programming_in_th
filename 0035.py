inp = int(input())
num = []
max = -999999

for i in range(inp):
    num.append(list(map(int, input().split())))

for i in range(1, 2**inp):
    b = bin(i)[2:].zfill(inp)
    # print(b)  # 01 10 11
    temp = []
    for ii in range(len(b)):
        if b[ii] == "1":
            temp.append(num[ii])

    if len(temp) == 3:
        # print(temp)
        result = (abs((temp[0][0] * temp[1][1]) + (temp[1][0] * temp[2][1]) + (temp[2][0] * temp[0][1]) - (
            temp[0][1] * temp[1][0]) - (temp[1][1] * temp[2][0]) - (temp[2][1] * temp[0][0]))) / 2
        # print((temp[0][0] * temp[1][1]))
        # print(temp, result)
        if result > max:
            max = result
print("%.3f" % max)
