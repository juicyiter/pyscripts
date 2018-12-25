# coding: utf-8

print('This {food} is {adjective}'.format(food='spam', adjective='absolutely horrible'))

print('The story of {0}, {1}, and {other}.' . format('Bill', 'Manfred', other='Gerog'))

table = {'Sjoerd': 123, 'Jack': 2038, 'Dcab': 8030}

print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab:{0[Dcab]:d}'.format(table))

print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab:{Dcab:d}'.format(**table))

hello = '你好'

number = 133

print(f'The string is {hello:^010} and the number is {number:^09.2f}')
print(f'The raw(call repr on ) string is {hello!r}')
print('The ASCII code of string is {0!a}'.format(hello))

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).ljust(3), end=' ')
    print(repr(x*x*x).rjust(4))

