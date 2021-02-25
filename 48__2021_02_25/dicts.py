s = input()
counts = {}
while s != "stop":
    if s in counts:
        counts[s] += 1
    else:
        counts[s] = 1
    s = input()
print(counts)