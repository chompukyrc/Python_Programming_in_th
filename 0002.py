min = 2000000000
max = -2000000000

n = int(input())

num = []
for i in range(n):
    inp = int(input())
    num.append(inp)


# print(num)
for i in range(len(num)) : 
    # print(i)
    if num[i] < min :
        min = num[i]
    if num[i] > max :
        max = num[i]
    
print(min)
print(max)
