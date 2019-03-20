import string

values = {'val': 'foo'}

t = string.Template('$val is here, but $missing is not.')

try:
    print('Template:   ', t.substitute(values))
except KeyError as Err:
    print('Error:', str(Err))

print('Template:', t.safe_substitute(values))
