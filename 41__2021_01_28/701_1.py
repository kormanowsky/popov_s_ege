"""
Дан текстовый файл, в котором находятся только строчные латинские буквы,
десятичные цифры, знаки препинания (,;:-?!) и пробелы, всего не более
10^6 символов. Будем называть словом любую последовательность из букв и цифр,
не обязательно осмысленную.
a. С клавиатуры вводится натуральное число N. Сколько слов длины N или более
в этом файле?
b. Сколько слов в этом файле содержат три или более гласных буквы?
c. Какая буква встречается чаще, a или o?
d. Чему равна сумма всех цифр, находящихся в этом файле?
"""

"""
Пункт с
"""
print("Ответ на пункт C:")
count_a = 0
count_o = 0
with open("input.txt", "r") as file:
    # В s читается каждый символ
    s = file.read(1)
    while s:
        if s == "a":
            count_a += 1
        elif s == "o":
            count_o += 1
        s = file.read(1)
if count_a > count_o:
    print("Чаще встречается буква a")
elif count_a < count_o:
    print("Чаще встречается буква o")
else:
    print("Буквы а и о встречаются одинаковое число раз")

"""
Пункт а.
"""
count_words = 0
current_word_len = 0
n = int(input("Введите N для пункта A:\n"))
print("Ответ на пункт A:")
with open("input.txt", "r") as file:
    # В s читается каждый символ
    s = file.read(1)
    while s:
        if s.isalpha() or s.isdigit():
            current_word_len += 1
        else:
            if current_word_len >= n:
                count_words += 1
            current_word_len = 0
        # Переходим к новому символу
        s = file.read(1)
    if current_word_len >= n:
        count_words += 1
print(count_words)

"""
Пункт b.
"""
vowels = ["a", "e", "i", "o", "u", "y"]
count_words = 0
current_vowels_len = 0
print("Ответ на пункт B:")
with open("input.txt", "r") as file:
    # В s читается каждый символ
    s = file.read(1)
    while s:
        if s.isalpha() or s.isdigit():
            if s in vowels:
                current_vowels_len += 1
        else:
            if current_vowels_len >= 3:
                count_words += 1
            current_vowels_len = 0
        # Переходим к новому символу
        s = file.read(1)
    if current_vowels_len >= 3:
        count_words += 1
    current_vowels_len = 0
print(count_words)

"""
Пункт d.
"""
digits_sum = 0
print("Ответ на пункт D:")
with open("input.txt", "r") as file:
    # В s читается каждый символ
    s = file.read(1)
    while s:
        if s.isdigit():
            digits_sum += int(s)
        # Переходим к новому символу
        s = file.read(1)
print(digits_sum)
