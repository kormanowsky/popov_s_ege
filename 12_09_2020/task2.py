"""
2.	Иван получил зарплату в K и доходы от вклада в размере T. Налоговые правила государства,
в котором живет Иван – следующие: если доход жителя за месяц не превышают L,
то ставка налога равна 6%, иначе – 8%. Найти, сколько налогов нужно заплатить Ивану за этот месяц.
"""
k = int(input())
t = int(input())
l = int(input())
if k + t <= l:
    print(0.06 * (k + t))
else:
    print(0.08 * (k + t))
