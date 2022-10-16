student = {'name':'John', 'age': 25, 'courses': ['Math', 'CompSci'] } #name=key

print(student['courses']) #taking item
print(student.get('name'))
print(student.get('phone', 'Not found')) 

#appending new element & changing items
# student['phone'] = '666-666-666'
# student.update({'name': 'Slytherina', 'age': 22, 'adress': 'St 66 Hellmouth'})
# del student['age']
# adress = student.pop('adress')
# print(student)
# print(adress)

print(student.keys())
print(student.items())

for i in student: #only keys
    print(i)

for keys, items in student.items():
    print(items)