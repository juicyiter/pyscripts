age = 20
name = "Ethan"


print("{0} was {1} years old".format(name, age))
print("Why {0} is playing python?".format(name))

# Numbers can be omited
print("{} was {} years old".format(name, age))
print("Why is {} typing this?".format(name))

# Decimal with precison of 4 for float number.
print("{0:0.5}".format(1.0 / 3))

# Fill undercore(_) with the text centered
# (^) to 20 width
print("{0:_^20}".format("hello world"))

# Keyword base
print("{name} is typing with {keyboard}.".format(
    name="Ethan", keyboard="poker"))
r'''
Note
 When formatting a number (int, float, complex, decimal.Decimal and subclasses)
 with the n type (ex: '{:n}'.format(1234)), the function
 temporarily sets the LC_CTYPE locale to the LC_NUMERIC locale to
 decode decimal_point and thousands_sep fields of localeconv()
 if they are non-ASCII or longer than 1 byte, and
 the LC_NUMERIC locale is different than the LC_CTYPE locale.
 This temporary change affects other threads.

 Changed in version 3.7: When formatting a number with the n type,
 the function sets temporarily the LC_CTYPE locale to the LC_NUMERIC locale in some cases.
'''

print('{name} was born in {country}'.format(**{'name': 'Guido', 'country': 'UK'}))

print('{name} was born in {country}'.format_map({'name': 'Guido', 'country': 'UK'}))

# End with a blank
# print('a', end = '') to be solved

# Escape character
print("This is line one.\nAnd this is line two.")
print("what's your name?")

# Note the differences
print('What\'s your name?')

# Raw text
print(r"This is a raw text. \n")
