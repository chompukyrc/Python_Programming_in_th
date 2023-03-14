inp = input()
inp = " " + inp + " "

aeiou = {"a", "e", "i", "o", "u"}

i = 1

while i < len(inp) - 1:
    if inp[i] != "p":
        print(inp[i], end="")
        i += 1 
        continue

    if inp[i-1] == inp[i+1] and inp[i+1] in aeiou:
        i += 2
        continue

    print("p",end='')
    i+=1

