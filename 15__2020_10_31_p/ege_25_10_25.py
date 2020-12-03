"""
Отрезок [185 311; 185 330]. На нем найти все числа, у которых ровно 4 делителя.
"""
for x in range(185311, 185331):
    deliteli = []
    for j in range(1, x+1):
        if x % j == 0:
            deliteli.append(j)
    if len(deliteli) == 4:
        # print(deliteli[0], deliteli[1], deliteli[2], deliteli[3])
        print(*deliteli)