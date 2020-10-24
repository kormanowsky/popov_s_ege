def flowers(n, a, b, c):
    if n == 1:
        return a
    if n == 2:
        return b
    if n == 3:
        return c
    return flowers(n-1, a, b, c) + flowers(n-2, a, b, c) + flowers(n-3, a, b, c)


a, b, c = map(int, input().split())
n = int(input())
print(flowers(n, a, b, c))