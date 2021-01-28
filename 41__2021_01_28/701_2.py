"""
Мама дала Пете Х рублей и попросила его купить в магазине фрукты:
яблоки и апельсины. Яблоко стоит 24 рубля, а апельсин – 27 рублей.
Петя очень любит апельсины и поэтому хочет купить их как можно больше, но мама
попросила, чтобы каждого фрукта было хотя бы по одному, а сдачи было не более
10 рублей. Для каждого натурального Х из отрезка [450, 500] нужно посчитать
и вывести количество способов покупки фруктов и максимальное количество
апельсинов, которое может купить Петя на Х рублей с учетом всех условий мамы.
"""
apple_cost = 24
orange_cost = 27

for money in range(450, 501):
    ways_count = 0
    max_oranges = 1
    max_apples = money // apple_cost
    for apples_count in range(1, max_apples + 1):
        oranges_count = (money - apple_cost * apples_count) // orange_cost
        change = money - apple_cost * apples_count - orange_cost * oranges_count
        if oranges_count >= 1 and change <= 10:
            ways_count += 1
            if oranges_count > max_oranges:
                max_oranges = oranges_count

    print(ways_count, max_oranges)