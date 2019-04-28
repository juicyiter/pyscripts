import textwrap

class TEXT_WRAP_EXAMPLE():
	def __init__(self):
		self.des = 'Description:\n'
		self.res = 'Results...\n'


	def sampleText(self):
		self.des = 'Sample text:'
		self.res = '''
	    The text wrap module can be  used to fromat text for output in
	        situations where pretty-printing is desired. It offers
	    programatic functionality similar to the paragraph wrapping
	    orfilling features found in many text editors.
	    '''
		return self.res


	def fillParagraph(self):
		self.des = 'Filling paragraph:'
		self.res = textwrap.fill(self.sampleText(), width=70)
		return self.res


	def remvIndents(self):
	    
	    # The result is a block of text with *initial whitespace from each line removed
	    '''
	    _line_one
	    ___line_two
	    _line_three
	    '''
	    # becomes
	    '''
	    line_one
	    __line_two
	    line_thre
	    ''' 
	    self.des = 'Removing existing indents:'
	    self.res = textwrap.dedent(self.sampleText())
	    return self.res


	def fillAndDedent(self):
	    dedented_text = self.remvIndents()
	    self.des = 'Combining fill and fill:'
	    self.res = textwrap.fill(dedented_text, width=50)
	    return self.res


	def indent(self):
	    wraped = self.fillAndDedent() + '\n     \nSecond paragraph after a blank line'
	    self.des = 'Indenting Blocks:'
	    self.res = textwrap.indent(wraped, '>')
	    return self.res

	def indentPredict(self):
		self.res = 'Control which line to indent:'
		sample = self.sampleText()

		def should_indent(line):
	        # print raw line
			print('Indent {!r}?'.format(line))
			return len(line.strip()) % 2 == 0


		print('\nQuoted:\n')
		wraped = self.fillAndDedent()
		self.res = textwrap.indent(wraped, 'EVEN', predicate=should_indent)
		return self.res


	def hang_indents(self):
		dedented_text = self.remvIndents()
		self.des = 'Haning indents:'
		self.res = textwrap.fill(dedented_text,
								 initial_indent='',
								 subsequent_indent='*'*4,
								 width=50,)


	def shorten_text(self):
		original = self.remvIndents()
		shortened = textwrap.shorten(original, 100)
		shorten_wrapped = textwrap.fill(shortened, width=50)
		print(shorten_wrapped)

	def latest(self):
		return self.shorten_text()
	def __repr__(self):
		return self.des + '\n\n' + self.res + '\n'

EXAMPLE = TEXT_WRAP_EXAMPLE()
EXAMPLE.latest()
# print(EXAMPLE)
