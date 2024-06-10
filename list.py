numbers = [1,3,9,7,2,4,5,6]
# print(numbers[2:5:2])
# print(numbers[5:2:-2])
# print(numbers[:])
# print(numbers[::-1])
numbers.append(13)
numbers.insert(3,11)
if 1 in numbers:
    numbers.remove(1)
print(numbers)
if 7 in numbers:
    index=numbers.index(7)
    print(index)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)