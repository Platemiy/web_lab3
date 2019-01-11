# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        self.items=items
        self.ignore_case=False
        if 'ignore_case' in kwargs:
            self.ignore_case=bool(kwargs['ignore_case'])
        self.index=-1
        self.unique_items=[]
        for i in self.items:


            if i not in self.unique_items:
                if (not self.ignore_case):
                    self.unique_items.append(i)
                else:
                    if type(i)==str:
                        if i.lower() in self.unique_items: continue
                        else: self.unique_items.append(i.lower())
                    elif i not in self.unique_items: self.unique_items.append(i)
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False


    def __next__(self):
        # Нужно реализовать __next__
        if self.index==len(self.unique_items)-1:
            raise StopIteration
        self.index+=1
        return self.unique_items[self.index]



    def __iter__(self):
        return self
