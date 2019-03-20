import string
t = string.Template('$var')
print(t.pattern.pattern)
r'''
    \$(?:
      (?P<escaped>\$) |   # Escape sequence of two delimiters
      (?P<named>(?-i:[_a-zA-Z][_a-zA-Z0-9]*))      |   # delimiter and a Python identifier
      {(?P<braced>(?-i:[_a-zA-Z][_a-zA-Z0-9]*))}   |   # delimiter and a braced identifier
      (?P<invalid>)              # Other ill-formed delimiter exprs
    )
'''
