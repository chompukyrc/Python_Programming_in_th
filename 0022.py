inp = int(input())

if inp % 2 == 0:
    for i in range(inp//2):
        for j in range(inp-1):    
            if j==(inp//2)-1-i or j==(inp//2)-1+i:
                print("*", end="")
            else:
                print("-", end="")
        print("")

    for i in range(inp//2-1, -1, -1):
        for j in range(inp-1):    
            if j==(inp//2)-1-i or j==(inp//2)-1+i:
                print("*", end="")
            else:
                print("-", end="")
        print("")

else:
    for i in range(inp//2+1):
        for j in range(inp):
            if j==(inp//2)-i or j==(inp//2)+i:
                print("*", end="")
            else:
                print("-", end="")
        print("")

    for i in range(inp//2-1, -1, -1):
        for j in range(inp):
            if j==(inp//2)-i or j==(inp//2)+i:
                print("*", end="")
            else:
                print("-", end="")
        print("")