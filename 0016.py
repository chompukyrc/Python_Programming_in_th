adrian = ["A", "B", "C"]
Bruno = ["B", "A", "B", "C"]
Goran = ["C", "C", "A", "A", "B", "B"]

count_A = 0
count_B = 0
count_G = 0

num = int(input())
inp = input()

for i in range(len(inp)):
    if inp[i] == adrian[i%3]:
        count_A += 1
    if inp[i] == Bruno[i%4]:
        count_B += 1
    if inp[i] == Goran[i%6]:
        count_G += 1

max_max = max(count_A, count_B, count_G)
print(max_max)
if max_max == count_A:
    print("Adrian")
if max_max == count_B:
    print("Bruno")
if max_max == count_G:
    print("Goran")