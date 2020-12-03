"""
Даны N натуральных чисел (N дается в первой строке).
Вывести те из них, которые заканчиваются на 7 и десятичная
запись которых содержит хотя бы одну цифру 4.
"""
N = int(input())
for i in range(N):
    x = int(input())
    if x % 10 == 7:
        has_four = False
        x_copy = x
        while x > 0 and not has_four:
            if x % 10 == 4:
                has_four = True
            x //= 10
        x = x_copy
        if has_four:
            print(x)
