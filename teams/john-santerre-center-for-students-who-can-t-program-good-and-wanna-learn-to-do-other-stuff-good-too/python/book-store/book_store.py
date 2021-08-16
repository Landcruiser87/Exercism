#%%

def total(basket:list)->int:
	"""[Function for calculating lowest cost combination of books.\n
		Thought process.\n
		1.  Reduce basket to its unique components until nothing is left.
		2.  Eliminate edge cases (4&4 cheaper than 5&3)
		3.  Calculate total discount for each unique group
		4.  Do Happy Dance
		]

	Args:
		basket ([list]): [List of books to buy]
	"""	
	DISCOUNT = {
			1: 1, 
			2: 0.95, 
			3: 0.9, 
			4: 0.8, 
			5: 0.75
	}
	groups = []
	while len(basket) !=0:
		grouped = set(basket)
		groups.append(len(grouped))
		[basket.remove(book) for book in grouped]

	while 3 in groups and 5 in groups:
		groups[groups.index(3)] = 4
		groups[groups.index(5)] = 4

	total = sum([(book * 800) * DISCOUNT[book] for book in groups]) 
	return total