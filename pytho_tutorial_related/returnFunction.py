def createCounter():
    i = 0
    def counter():
        nonlocal i
        i += 1
        return i
    return counter
def lazy_sum(*args):
    ax = 0
    def sum():
        for n in args:
            nonlocal ax
            ax += n
        return ax
    return sum
a = lazy_sum(1, 2, 4)
c = createCounter()
print(a())
print(c(), c(), c())
