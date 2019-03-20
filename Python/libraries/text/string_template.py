import string


values = {'var': 'foo', 'int': 1}
# val = 'foo'

# var inside works like a key
# No formatting options are available
t = string.Template('''
Variable: $int
Escape: $$
Variable in text: ${var}iable
''')
print(t.substitute(values))

s = '''
Variable: %%%(int)d
Escape: %%
Varaible in text: %(var)siable
'''
print(s % values)


print('{:.4}'.format(1.3))
values = {'var': 'foo', 'float': 1.3}
s = '''
Variable: {float:.42}
Escape: {{}}
Variable in text: {var}iable
'''
# what does '**' do????
print(s.format(**values))
