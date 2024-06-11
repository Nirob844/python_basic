# def double (x):
#     return x*2

double = lambda num: num*2

result = double(44)
print(result)

numbers = [1,3,9,7,2,4,5,6]
double_nums = map(double, numbers)
print(list(double_nums))

actors = [
    {'name':'sakib','age':40},
    {'name':'rajjak','age':75},
    {'name':'manna','age':60},
    {'name':'riyaz','age':44},
]

juniors = filter(lambda actor: actor['age']<45, actors)
print(list(juniors))