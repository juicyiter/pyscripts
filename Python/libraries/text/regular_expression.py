import re

pattern = 'this'
text = 'Does this text match the pattern?'

match = re.search(pattern, text)

s = match.start()
e = match.end()

print('Found "{}"\n in "{}"\n form {} to {} ("{}")'.format(
	match.re.pattern, match.string, s, e, text[s:e]))

# Multiple matches

text = 'abbaaabbbbaaaaa'
pattern = 'ab'

for match_iter in re.finditer(pattern, text):
	print('Found {!r} in text: {!r} at {}'.format(match_iter, text, match_iter.start()))

for match_string in re.findall(pattern, text):
	print('Found {!r}'.format(match_string))


# Find each pattern in text, and print them out
def test_patterns(patterns, text):

	for pattern, desc in patterns:
		print("'{}' ('{}') \n".format(pattern, desc))
		print(text)
		for match_iter in re.finditer(pattern, text):
			s = match_iter.start()
			e = match_iter.end()
			# number of escape characters
			num_backslashes = text[:s].count('\\')

			print('.'*(num_backslashes + s) + text[s:e])

test_patterns([('ab', "'b' after 'a'"), ('bb', "double 'b'")], 'abbaaabbbbaaaaa')