import textwrap

sample_text = '''
    The textwrap module can be used to format text form ouput in
    situations where pretty-printing is desired.  It offers
    programmatic functionality similar to the paragraph wrapping
    or filling features founud in many text editors.
    '''
# Filling paragraphs
print(textwrap.fill(sample_text, width=50))
