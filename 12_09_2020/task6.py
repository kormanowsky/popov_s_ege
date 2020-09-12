"""
6.	Петя живет в доме, в котором N подъездов, M этажей и K квартир.
На каждом этаже каждого подъезда одинаковое число квартир, так что K делится на M * N.
Номер квартиры Пети – X. Найти, в каком подъезде и на каком этаже живет Петя.
"""
n = int(input())
m = int(input())
k = int(input())
x = int(input())

flats_per_floor = k // (m * n)
flats_per_entrance = flats_per_floor * m
petya_entrance = (x - 1) // flats_per_entrance + 1
petya_floor = (x - 1 - (petya_entrance - 1) * flats_per_entrance) // flats_per_floor + 1
print(petya_entrance, petya_floor)
