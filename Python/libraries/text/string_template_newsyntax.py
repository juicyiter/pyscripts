# import re
import string


class MyTemplate(string.Template):
    delimiter = '{{'
    pattern = r'''
    \{\{(?:
    (?P<escaped>\{\{)|
    (?P<named>[_a-z][a-z0-9]*)\}\}|
    (?P<braced>[_a-z][a-z0-9]*)\}\}|
    (?P<ignored>)
    )
    '''


t = MyTemplate('''
    {{{{
    {{var}}
    ''')
print('Matches:', t.pattern.findall(t.template))

print('Substituted:', t.substitute(var='replacement'))
