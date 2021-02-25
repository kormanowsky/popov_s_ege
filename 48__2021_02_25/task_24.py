s = "CBCABABACCC"
counts = {}
for i in range(len(s) - 2):
    left = s[i]
    center = s[i + 1]
    right = s[i + 2]
    if left != right:
        continue
    if center in counts:
        counts[center] += 1
    else:
        counts[center] = 1

max_count = 0
max_count_symbol = None
for symbol in counts:
    if counts[symbol] > max_count:
        max_count = counts[symbol]
        max_count_symbol = symbol

print(max_count_symbol)
