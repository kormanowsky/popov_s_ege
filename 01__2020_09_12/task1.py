"""
1.	Дано число X. Выяснить, трехзначное оно (тогда вывести YES) или нет (вывести NO).
"""
x = int(input())
if 100 <= x <= 999:
    print("YES")
else:
    print("NO")

# Или print("YES" if 100 <= x <= 999 else "NO")
