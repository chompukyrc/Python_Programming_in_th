# inp = [7, 8, 10, 13, 15, 19, 20, 23 ,25]
inp = []
for _ in range(9):
    inp.append(int(input))

for i in range(1, 2**9):
    b = bin(i)[2:].zfill(9)
    # print(b)
    temp = []
    for ii in range(len(b)): #111111000
        if b[ii] == "1":
            temp.append(inp[ii])
    if len(temp) == 7 and sum(temp)==100:
        for t in temp:
            print(t)