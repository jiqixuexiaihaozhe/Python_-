import collections

class Company:
    def __init__(self, employees):
        self.employees = employees

    def __getitem__(self, item):
        return self.employees[item]
company = Company(['a','b','c'])
print(isinstance(Company,collections.Iterable))

# 好神奇，明明company不是可迭代对象，却可以用for循环。而comapny.employees才是可迭代对象。
#因为__getitem()__也是个魔法函数
for val in company:
    print(val)
company1 = company[:2]
for val in company1:
    print(val)