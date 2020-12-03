min_k = 10415
count_k = 0
for k in range(4668, 10415):
    if (k % 3 == 0 or k % 11 == 0) and k % 2 != 0 \
        and k % 13 != 0 and k % 22 != 0 and k % 33 != 0:
        count_k += 1
        if k < min_k:
            min_k = k
print(count_k, min_k)