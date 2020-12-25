# Файл должен существовать, иначе будет ошибка
f = open("text3.txt", "r")
i = 0
for line in f:
    print(i, line, end="")
    i += 1
