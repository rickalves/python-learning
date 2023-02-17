# It's not recommended to use arrays in python, switch it for numpy lib
import array as arr
numbers = arr.array('d', [3, 5, 4.5])

print(repr(numbers))
print(numbers[2])
numbers.append(8.7)
print(repr(numbers))