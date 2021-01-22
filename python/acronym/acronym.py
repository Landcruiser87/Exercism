def abbreviate(words):
	'''
	Replace , _ and - with either no space or a space
	split the words based on space
	List comprehension to extract uppercase of first letter of each word in list
	return the joined list to form acronym.

	'''
	words = ''.join(words.split(','))
	words.replace("'", " ")
	words = ''.join(words.split('_'))
	words = ' '.join(words.split('-'))

	words = words.split()
	
	ABR = [word[0].upper() for word in words]
	return ''.join(ABR)
