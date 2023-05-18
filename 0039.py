def permu(a, k=0):
    if k == len(a):
        # print(a[0])
        if not (a[0] in ban):

            all_permu.append(a.copy())
    else:
        for i in range(k, len(a)):
            a[k], a[i] = a[i], a[k]
            permu(a, k+1)
            a[k], a[i] = a[i], a[k]


inp = int(input())
num = int(input())
ban = list(map(int, input().split()))
# inp = 4
# num = 3
# ban = [1, 2, 3]
food = []
all_permu = []

for i in range(1, inp+1):
    food.append(i)

permu(food)
# print(all_permu)

all_permu.sort()
for j in all_permu:
    print(*j)
