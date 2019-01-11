#!/usr/bin/env python3
from librip.gens import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 3, 10)
data3 = ['A','a','B','b','B','a','A','b']

# Реализация задания 2
myit1=Unique(data1)
for i in myit1:
    print(i, end=' ')
print('\n')
myit2=Unique(data2)
for i in myit2:
    print(i, end=' ')
print('\n')
myit31=Unique(data3)
for i in myit31:
    print(i, end=' ')
print('\n')
myit32=Unique(data3,ignore_case=True)
for i in myit32:
    print(i, end=' ')