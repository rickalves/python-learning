#sorting list in python

# creating example base lists
ages = [56, 90 ,33, 14, 78, 94]
users = ["Rick", "Mary", "Clara", "Lara", "Fernanda", "Matheus"]
books = [
    ("Art of War", 1850),
    ("Clean Code", 2003),
    ("Design Pattern", 2006)
]


# sort books by year
print(sorted(books, key=lambda book: book[1], reverse=True))
#sort ages by reverse order
print(sorted(ages, reverse=True))
print(list(reversed(ages)))

# sort user by alphabetical order
print(sorted(users))

#using list sort method(Modifing the list)
ages.sort()
print(ages)
ages.reverse()
print(ages)