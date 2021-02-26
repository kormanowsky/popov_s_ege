for x in range(7107, 7142):

    is_simple = True
    y = 2
    while y * y < x:
        if x % y == 0:
            is_simple = False
            break
        y += 1

    if is_simple:
        print(2 * x ** 2)
