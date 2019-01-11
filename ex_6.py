# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import json
import sys
from librip.ctxmngrs import timer
from librip.decorators import print_result
from librip.gens import field, gen_random
from librip.iterators import Unique as unique
from random import randint

path = u'C:\\Users\\User\\PycharmProjects\\web_lab3\\data_light_cp1251.json'

# Здесь необходимо в переменную path получить
# путь до файла, который был передан при запуске

with open(path) as f:
    data = json.load(f)


# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Важно!
# Функции с 1 по 3 дожны быть реализованы в одну строку
# В реализации функции 4 может быть до 3 строк
# При этом строки должны быть не длиннее 80 символов

@print_result
def f1(arg):
    return list(unique(field(arg,"job-name"),ignore_case=True))



@print_result
def f2(arg):
    return list(filter(lambda x:'программист' in x,arg))


@print_result
def f3(arg):
    return list(map(lambda x: x+' с опытом Python', arg))


@print_result
def f4(arg):
    return list(zip(arg,['зарплата {} руб.'.format(str(randint(100000,200000))) for x in range(len(arg))]))


with timer():
   f4(f3(f2(f1(data))))
