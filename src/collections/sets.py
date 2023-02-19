# Working with SET data type
#  A set is an unordered collection with no duplicate elements


studentsA = {45, 23, 78, 90, 78, 45, 90, 50}
studentsB = {12, 53, 23, 45, 10, 12, 76, 88}

# unique sets of A and B
print(f'A:{studentsA}')
print(f'B:{studentsB}\n')
# set operations
# studentsA not in studentsB
print(f'A - B:{studentsA - studentsB}')

# students in A or B or both
print(f'A | B:{studentsA | studentsB}')
# studens in A and B
print(f'A & B:{studentsA & studentsB}')
# studens in A and B but not in both
print(f'A ^ B:{studentsA ^ studentsB}')

# other set operations

# add not duplicate elements
studentsB.add(200) #added
studentsA.add(23) #not added

print(f'A:{studentsA}')
print(f'B:{studentsB}')