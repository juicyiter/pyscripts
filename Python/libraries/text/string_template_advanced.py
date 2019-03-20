import string


class MyTemplate(string.Template):
    delimiter = '%'
    # variable name must include an underscore
    # somewhere in the middle
    idpattern = '[a-z]+_[a-z]+'


template_text = '''
Delimiter : %%
Replaced  : %with_underscore
Ignored	  : %notunderstood
'''

d = {'with_underscore': 'replaced',
     'notunderstood': 'not replaced'}

t = MyTemplate(template_text)

print('Modified ID pattern:')
print(t.safe_substitute(d))
# ValueError: Invalid placeholder in string
# print(t.substitute(d))
