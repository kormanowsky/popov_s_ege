def F(n):
    if n % 5 > 3:
        return G(n // 5)
    return G(n // 2)


def G(n):
    if n > 1:
        return n + F(n - 1)
    return n


print(F(102))
