# Immutable
first_name = "Yuriy"
print(first_name[2])
# first_name[2] = 'l'
# print(first_name)

first_two_letters = first_name[:2]
print(first_two_letters)
last_letter = first_name[-2:]
print(last_letter)

# Concatenable
new_first_name = first_two_letters + 'l' + last_letter
print(new_first_name)

greeting = 'Hello'
greeting = greeting + ' Python!'
print(greeting)

# Multiplication
yummy = 'Yum '
print(yummy * 2)

print(yummy.upper())
print(yummy.lower())
print(yummy)