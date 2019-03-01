#!/opt/local/bin/python
# _*_ coding: utf-8 _*_

'Metaclass'

__author__ = 'Ethan Mengoreo'


def fn(self, name='World'):
    print('Hello, %s' % name)

'''Create hello class'''
'''
Three arguments in type:
1.Class name
2.Tuple of super class
3.Dictionary of methods bounded to their name
'''
Hello = type('Hello', (object,), dict(hello=fn))

h = Hello()
'''Hello, world'''
h.hello()

'''<class '__main__.Hello'> <class 'type'>'''
print(type(h), type(Hello))




'''Metaclass'''
class ListMetacalss(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass=ListMetacalss):
    pass

L = MyList()
L.add(1)

'''[1]'''
print(L)

L2 = list()
''' AttributeError: 'list' object has no attribute 'add' '''
L2.add(1)
