x = int(input())
d = 0
while x > 0:
    d = d * 10 + x % 3
    x //= 3
print(d)
