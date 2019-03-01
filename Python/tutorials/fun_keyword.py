# we use the name keyword instead of position to specify
# the arguments to the function

def func(a, b = 10, c = 40):
    print("a is", a, ", b is", b, "and c is",  c)

func(2, 3)

func(23, c = 20)

# func(c = 20, b = 30) :Error: missing 1 required positional argument : 'a'

func(a = 2, b = 3, c = 4)

func(c = 30, a = 100) # note the order!x

