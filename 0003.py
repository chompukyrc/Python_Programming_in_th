m = int(input())
n = int(input())

# print(m, n)
num = [[0] * m for i in range(n)]
# num2 = [[0] * m for i in range(n)]

for i in range(n) :
    for j in range(m) :
        inp = int(input())
        num[i][j] = inp
        # print(i, j, num[i][j], inp)
        # print(num)

for i in range(n) :
    for j in range(m) :
        inp = int(input())
        num[i][j] = inp + num[i][j]
        print(num[i][j], end=" ")
    print("")
        

# print(num)
# print(num2)
