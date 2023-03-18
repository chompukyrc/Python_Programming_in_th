a, b, c = map(int, input().split())
num = [a, b, c]
count = 0

while num[0] > 1 or num[1] > 1 or num[2] > 1:
    num.sort(reverse=True)
    if num[0] % 2 == 1:
        num[0] = (num[0]-1) / 2
        count += 1
    else:
        num[0] = num[0]/2
        count += 1

print(count)
