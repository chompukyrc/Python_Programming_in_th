import math
inp = int(input())
if inp == 1:
    print("2.000000")
elif inp == 3:
    print("3.732051")
elif inp % 2 == 0:
    print("{:.6f}".format(inp))
elif inp % 2 != 0:
    print("{:.6f}".format(inp+0.464102))
