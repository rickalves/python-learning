# Dictionary is a set of key: value pairs;
# Keys are unique (within one dictionary);
tells = {
    "Rick": 7890,
    "Mary": 2342,
    "Lara": 5675, #ignored because the duplicated key
    "Lara": 7897
}

# print(tells)
# print(tells["Rick"])
# print(tells["Lara"]) #7897 not 5675

# another ways to get elements
# print(tells.get("Lara"))

# operations with dicts
tells["Rick"] = 2098
del tells["Lara"]
tells["John"] = 2342

print(tells)
print("Lara" in tells)

for tell, value in tells.items():
    print(f'{tell}:{value}')

# list manipulation
print_tells = [f'tell:{tell}' for tell in tells.values()]

print(print_tells)

# others ways to create dicts
courses = dict(name = "INFOR", duration = "2 years")
# print(courses)