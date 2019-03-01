age = 20
name = "Ethan"


print("{0} was {1} years old".format(name,age))
print("Why {0} is playing python?".format(name))

# Numbers can be omited
print("{} was {} years old".format(name,age))
print("Why is {} typing this?".format(name))

# Decimal with precison of 4 for float number.
print("{0:.4}".format(1.0/3))

# Fill undercore(_) with the text centered
# (^) to 20 width
print("{0:_^20}".format("hello world"))

# Keyword base
print("{name} is typing with {keyboard}.".format(name = "Ethan",keyboard = "poker"))

# End with a blank
# print('a', end = '') to be solved

# Escape character
print("This is line one.\nAnd this is line two.")
print("what's your name?")

# Note the differences
print('What\'s your name?')

# Raw text
print(r"This is a raw text. \n")

