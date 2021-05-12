def abbreviate(words):
	"""[Replace , _ and - with either no space or a space.  Splits the words based on space. List comprehension to extract uppercase of first letter of each word in list
	return the joined list to form acronym]

	Args:
		words ([str]): [words to be abbreviated]

	Returns:
		[str]: [Abbreviated string]
	"""
	words = ''.join(words.split(','))
	words.replace("'", " ")
	words = ''.join(words.split('_'))
	words = ' '.join(words.split('-'))

	words = words.split()
	
	ABR = [word[0].upper() for word in words]
	return ''.join(ABR)
