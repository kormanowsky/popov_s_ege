def f(n):
    # Условие выхода из рекурсии
    if n == 1 or n == 2:
        return 1
    else:
        return f(n - 1) + f(n - 2)


print(f(8))