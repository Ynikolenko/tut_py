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
print(yummy * 2) # вывести два раза

print(yummy.upper()) # вывести результат заглавными
print(yummy.lower()) # вывести результат маленькими
print(yummy)

long_string = 'Это самая длиная строка в программе'
print(long_string.split()) # разбивка строки по словам
print(long_string.split('а')) # убирает из строки символ
