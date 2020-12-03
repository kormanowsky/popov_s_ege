N = int(input())
min_el = -1
max_el = 0
sum_el = 0
for i in range(N):
    x = int(input())
    if min_el == -1:
        min_el = x
    elif x < min_el:
        min_el = x
    elif x > max_el:
        max_el = x
    sum_el += x
print(min_el, max_el, sum_el / N)