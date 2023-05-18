inp = int(input())
text = []
text_not_dup = []

for i in range(inp):
    text.append(input())
# print(text)

for x in text:
    if x not in text_not_dup:
        text_not_dup.append(x)
# print(text_not_dup)

text_not_dup.sort()
for t in text_not_dup:
    print(t)
