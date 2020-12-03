"""
5.	Сегодняшняя дата - D.M., где D – номер дня в месяце, M – номер месяца (счет ведется с 1). Сколько дней осталось
до нового года, если год невисокосный?
"""
d = int(input())
m = int(input())
answer = (d - 1) * -1
for i in range(m, 13):
    if i == 1:
        answer += 31
    elif i == 2:
        answer += 28
    elif i == 3:
        answer += 31
    elif i == 4:
        answer += 30
    elif i == 5:
        answer += 31
    elif i == 6:
        answer += 30
    elif i == 7:
        answer += 31
    elif i == 8:
        answer += 31
    elif i == 9:
        answer += 30
    elif i == 10:
        answer += 31
    elif i == 11:
        answer += 30
    elif i == 12:
        answer += 31
print(answer)