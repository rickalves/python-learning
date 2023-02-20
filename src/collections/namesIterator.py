# Using Generatos to create Iterators
# Using Genetatos to read files
def generateNames(file):
    names = open(f'./src/collections/{file}', 'r')
    for name in names:
        yield name
    names.close()

# creating a generate Obj
names = generateNames('names.log')

# show the file values
for name in names:
    print(name)