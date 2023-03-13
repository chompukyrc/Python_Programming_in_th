inp = list(input())
# print(inp)

is_upper = False
is_lower = False

for i in range(len(inp)) :
    if 65 <= ord(inp[i]) <= 90 :
        is_upper = True
    if 97 <= ord(inp[i]) <= 122 :
        is_lower = True

if is_upper == True and is_lower == False :
    print("All Capital Letter")
elif is_upper == False and is_lower == True :
    print("All Small Letter")
elif is_upper == True and is_lower == True :
    print("Mix")