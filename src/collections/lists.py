# Lists and list functions

numbers = [45, 78, 90, 54] #inicial list

print(45 in numbers)
print(repr(numbers))
numbers.append(55) #add an element at the end of list
print(repr(numbers))
numbers.remove(45) #remove the first element equal to 45
print(repr(numbers))
numbers.insert(3, 34)#insert an element at the given index
print(repr(numbers))
numbers.pop()#remove the last item in the list 
print(repr(numbers))
numbers.extend([90, 28, 17, 76, 99, 112]) # extend list by the list items
print(repr(numbers))

numbersAdd = [(number+1) for number in numbers] #add 1 for all number at the first list
print(repr(numbersAdd))
numbers2 = [(number) for number in numbers if number > 90] #create a new list with numbers greater then 90
print(repr(numbers2))
