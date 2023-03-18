inp = int(input())
arr = (list(map(int, input().split())))

# modes = statistics.multimode(arr)
# modes.sort()
# print(*arr)

freq_dict = {}
for element in arr:
    if element in freq_dict:
        freq_dict[element] += 1
    else:
        freq_dict[element] = 1

# Find the element(s) with the highest frequency
max_freq = max(freq_dict.values())
modes = list(filter(lambda x: freq_dict[x] == max_freq, freq_dict))
modes.sort()
print(*modes)
