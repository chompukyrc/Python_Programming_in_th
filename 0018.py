# inp = 15
# target = 12

inp, target = map(int, input().split())

def is_prime(n):
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True

arr = [0] * (inp+1)


for i in range(2,inp+1):
    if is_prime(i) and arr[i]==0:
        for j in range(i, inp+1, i):
            if arr[j] != 1:
                arr[j] = 1
                target -= 1
                if target == 0:
                    print(j)