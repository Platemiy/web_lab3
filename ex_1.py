#!/usr/bin/env python3
from librip.gens import field

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': 'Стелаж', 'price': 7000, 'color': 'white'},
    {'title': 'Вешалка для одежды', 'price': 800, 'color': 'white'}
]

# Реализация задания 1
genf=field(goods, 'title')
for i in genf:
    print('\'{}\''.format(i),end=' ')
print('\n')
genf2=field(goods, 'title', 'price')
for i in genf2:
    print(i,end=' ')
print('\n')
from librip.gens import gen_random
gr=gen_random(70, 100, 5)
for i in gr:
    print(i,end=' ')
