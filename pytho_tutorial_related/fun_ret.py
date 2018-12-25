def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return "The two numbers are equal."
    else:
        return y

    
print(maximum(1, 1))

# NOTE:
# A return statement without a value is equivalent to 'return None'
# `None` is a special type in Python that represents nothingness,
#  which is quite like `0` or `NULL` in C

def some_fun():
    pass
# The statement `pass` here is used to indicate an empty block of statements
# Every function implicitly contains a `return None` statement at the end
# unless you have written your own return statement

Excerpt From: Swaroop C H. “A Byte of Python.” iBooks. 
# 
print(some_fun())
