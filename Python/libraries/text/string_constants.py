import inspect
import string
import re


def is_str(value):
    return isinstance(value, str)


for name, value in inspect.getmembers(string, is_str):
    # inspect.getnumbers(object[, predicate])
    # Return all the members of an object in a list of (name, value) pairs sorted by name.
    # If the optional predicate argument is supplied, only members
    # for which the predicate returns a true value are included.
    if name.startswith('_'):
        continue
    print('%s=%r' % (name, value))


def titlecase(s):
    # what is mo?
    return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
                  lambda mo: mo.group(0)[0].upper() +
                  mo.group(0)[1:].lower(),
                  s)


titlecase("they're bill's friends.")
