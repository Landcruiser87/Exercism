def distance(strand_a, strand_b):
	'''
	Function to calculate Hamming distance of two strings
	Using a Generator Comprehension
	Zip the two files, sum those that are inequal for a hamming distance
	
	Args:
		strand_a:  DNA string 1
		strand_b:  DNA string 2
		a: index
		b: index
	Returns:
		sum of inequal characters.
	'''
	if len(strand_a) != len(strand_b):
		raise ValueError("Ahhhhh i'm melting, unequal.  ahhhh")
	return sum(a!=b for a, b in zip(strand_a, strand_b))


