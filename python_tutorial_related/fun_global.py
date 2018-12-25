x = 40

def fun():
    global x

    print("x is", x)

    x = 2

    print("x changes to", x)

fun()

print("Value of x is", x)