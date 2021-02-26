for x in range(1010, 1020, 2):
    divisors_count = 0
    y = 1
    while y * y <= x:
        if x % y == 0:
            if y % 2 == 0:
                divisors_count += 1
            z = x // y
            if z != y:
                if z % 2 == 0:
                    divisors_count += 1
        y += 1
    if divisors_count == 3:
        print('dc', divisors_count, 'ans', x)
