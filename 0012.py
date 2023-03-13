import math

inp = input()
# inp = "CHOM"
n = len(inp)
m = (5*n-(n-1))
# print(m, n)
arr = [["." for j in range(m)] for i in range(5)]

# print(arr)
for i in range(5):
    for j in range(m):

        ii = math.floor((math.floor(j/4) + 1) / 3)

        if (12*ii)-4 <= j <= 12*ii and j != 0 and j != m-1:
            chr = "*" 
            # chr = (math.floor(j/4))
        else:
            chr = "#"
            # chr = (math.floor(j/4))

        if (i == 0 or i == 4) and j%4 == 2:
            arr[i][j] = chr

        elif (i == 1 or i == 3) and (j%4 == 1 or j%4 == 3):
            arr[i][j] = chr
        
        elif i == 2 and (j%4 == 0 or j%4 == 4):
            arr[i][j] = chr

        elif i == 2 and j%4 == 2:
            arr[i][j] = inp[math.floor(j/4)]

# print(n%3)
if n%3 == 0:
    arr[2][m-1] = '*'

for i in range(5):
    for j in range(m):
        print(arr[i][j], end="")
    print()