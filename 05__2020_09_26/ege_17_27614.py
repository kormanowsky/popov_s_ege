count_k = 0
max_k = 0
k = 5883
while k <= 15906:
    if (k % 9 == 0 or k % 23 == 0) and k % 13 != 0 \
        and k % 18 != 0 and k % 19 != 0 and k % 22 != 0:
        count_k += 1
        if k > max_k:
            max_k = k
    k += 1
print(count_k, max_k)