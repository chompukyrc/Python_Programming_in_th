inp = int(input())
if inp == 1:
    print("2")
elif inp == 2:
    print("2")
else:
    if inp % 2 == 0:
        n = inp - 2
    else:
        n = inp - 1
    print(n*(n+1))
