def F(n):
    if n == 1:
        return 3
    if n % 2 == 0:
        return n + F(n // 2)
    return 3 * F(n - 1)


print(F(115))
