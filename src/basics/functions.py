# basic functions
def sum(a, b):
    return(a+b)

print(sum(45, 10))

def greeter(name):
    print(f'\nHi there {name}!')

greeter("Rick")

# Arbitrary Arguments, *args
def children(*kids):
  for kid in kids:
    print(f'{kid}')

children("Emil", "Tobias", "Linus")

# pass statement

def someFunction(args):
    pass