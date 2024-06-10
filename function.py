
#! default function
def double_it(num):
    result =num * 2
    print(result)
#todo double_it(5)

#! args
def do_a_lot(*args):
    print(args)
    for num in args:
        print(num)
#todo do_a_lot(4,5,6,7,8,9)

#! kargs        
def full_name (first,last,**addition):
    #print(addition['title'])
    for key, value in addition.items():
        print(key,value)
    name = f'full name is : {first} {last}'
    return name
name = full_name(first='abul',last='kha', addition="sulukha", title="hujur",title2='khajor')
#todo print(name)

#! return multiple things from an array
def a_lot(num1,num2):
    sum = num1 + num2
    mult = num1 * num2
    remain = num1 - num2
    #todo return [sum,mult,remain]
    return sum,mult,remain
everything = a_lot(10,5)
print(everything)