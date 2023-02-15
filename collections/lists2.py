# Enumerating list in python(builtin)
# range()
# enumerate()

ages = [56, 90 ,33, 14, 78, 94]
users = ["Rick", "Mary", "Clara", "Lara", "Fernanda", "Matheus"]

# for i in range(len(ages)):
#     print(i, ages[i])

# print(list(range(len(ages))))

# enumerating lists
print(list(enumerate(ages)))

for user in enumerate(users):
    print(user)

for key , user in enumerate(users):
    print(f'Key:{key} User:{user}')

#unpacking tuples with for loops 
books = [
    ("Art of War", 1850),
    ("Clean Code", 2003),
    ("Design Pattern", 2006)
]

# for name, year in books:
#     print(name)

for name, _ in books:
    print(name)