# Filename: variables.py
print("Filename: variables.py")

i = 5
print(i)
i = i+1
print(i)

s = '''This is a multi-line string.
This is the second line.'''

print(s)

s = "This is a string.\
This continues the last string."

print(s)
# Also note that the variable s is changed???? Or it's just been modified???
# Or it's been re-stated??? Think! Boy!

i = \
    10
print(i)

# Note that the following numbers are operands
2 + 3
4 * 4

# power
print("Power")
print(2 ** 2)

# divide
## Python 2.x will yeild 4 (same as the 'divide and floor in python 3.x),
## while python 3.x will yeild 4.333333333333
print("Divide, note the differences between the Python 2.x and Python 3.x")
print(13 / 3)

# divide and floor (Python 3.x)
## Default for Python 2.x
print("Divide and floor")
print(13 // 3)

# modulo
print("Modulo")
print(13 % 3)
print(-25.5 % 2.25)

# boolean NOT
print("Boolean NOT")
print(not 1) # False
print(not 0) # True

x = not 12
y = not 0

print(x)
print(y)

# boolean AND and OR
print("Boolean AND and OR")
print(x and y)
print(x or y)

# The rest is same as C
print("The rest is same as C")

print("Evaluation Order")

eva_ord = ''' lambda (what the hell is it????)

if - else

or

and

not x

in, not in, is, is not, <, <=, >, >=, !=, ==

|

^

&

<<, >>

+, -

*, /, //, %,

+x, -x, ~x (Positive, negative, and bitwise not)

**

x[index], x[index:index], x(arguments...), x.attribute (Subscription, slicing, call, attribute reference

(expressions...), [expressions..], {key: value...}, {expressions...} (Binding or tuple display, list display, dictionary display, set display
