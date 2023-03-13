m, n = map(int, input().split())
A = [[0]*n for _ in range(m)]
B = [[0]*n for _ in range(m)]

for i in range(m):
    A[i] = list(map(int, input().split()))
    # print(A)

for i in range(m):
    B[i] = list(map(int, input().split()))

# print(A, B)

for i in range(m):
    for j in range(n):
        print(A[i][j] + B[i][j], end=" ")
    print()