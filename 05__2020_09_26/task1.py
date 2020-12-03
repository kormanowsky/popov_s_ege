N = int(input())
array = []
for i in range(N):
    array.append(int(input()))
min_el = -1
sum_el = 0
min_el_index = -1
for i in range(N):
    el = array[i]
    if el % 5 == 0:
        if min_el == -1 or el < min_el:
            min_el = el
            min_el_index = i
        sum_el += el
print(min_el, min_el_index, sum_el)