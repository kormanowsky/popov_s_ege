max_n = 0
count_n = 0
for n in range(4197, 9183):
    if n % 5 == 0 and n % 10 != 0 and n % 6 != 0 and n % 13 != 0 and n % 16 != 0:
        count_n += 1
        max_n = n
print(count_n, max_n, sep="")