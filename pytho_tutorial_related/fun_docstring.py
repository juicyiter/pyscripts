def print_max(x, y):
    '''This function prints the maximum of two numbers.

    The two values must be integers.'''
    
    # convert to integers if necessory.

    x = int(x)
    y = int(y)

    if x > y:
        print(x, "is maximum.")
    elif x == y:
        print("They are equal.")
    else:
        print(y, "is maximum.")


print_max(3, 6)
print_max(3, 3)

print(print_max._doc_)


# “A string on the first logical line of a function is the docstring for that function.”



## This function is problemetic!!!!!!!!
