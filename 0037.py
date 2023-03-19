import math
N, M = map(int, input().split())
L, K = map(int, input().split())
amount = int(input())

price = 0
for i in range(N):
    price += sum(list(map(int, input().split())))

print(math.ceil(((L*K*amount)+price)/amount))
