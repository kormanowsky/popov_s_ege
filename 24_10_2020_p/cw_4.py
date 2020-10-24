for n in range(95632, 95701):
    divisors = []
    for i in range(2, n+1):
        if n % i == 0 and i % 2 == 0:
             divisors.append(i)
    if len(divisors) == 6:
        print(*divisors)
        # print(divisors[0], divisors[1], ..., divisors[5])
