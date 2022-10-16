from collections import Counter
# c = Counter('Python on Python')
# print(c.most_common(3))
# print(c)
# c = Counter(['a', ' a', 'b', 'b', 'b', 'c'])
# d = ['a', 'b', 'b', 'c'] #odejmowanie
# # c.subtract(d)
# print(c)
# c.update(d)
# print(c)
# print(c)
# c = Counter({'a':2, 'b':1, 'c':2})
# print(c)
c = Counter(cats=2, dogs=4)
print(c['cats']) # nie wywala się, tylko zero
print(type(c['pets']))

#print(list(c.elements()))

