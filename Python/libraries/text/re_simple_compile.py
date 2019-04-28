# The compile() function converts 
# an expression string into a RegexObject

import re

# Precompile the patterns
# By precompiling all of the expressions when the module 
# is loaded, the compilation work is shifted t application start time
# instead of occurring at a point where the program may be responding
# to a user action.
regexes = [
	re.compile(p)
	for p in ['this', 'that']
]

text = 'Does this text mathc The pattern?'

print('Text: {!r}\n'.format(text))

for regex in regexes:
	print('Seeking "{}" ->'.format(regex.pattern), end=' ')

	if regex.search(text):
		print('Match!')
	else:
		print('No match')

print(dir(regexes[0]))