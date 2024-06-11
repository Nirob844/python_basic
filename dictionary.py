person = {
    'name': 'kala',
    'address': 'fala',
    'age':'20',
}
person['job']='facebooker'
print(person['age'])
del person['age']
print(person)

for key, value in person.items():
    print(key, value)