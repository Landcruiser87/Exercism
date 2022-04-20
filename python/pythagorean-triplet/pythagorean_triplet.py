def triplets_with_sum(number):
	"""This is a brute force approach for calculating all the combinations 
	that satisfy the conditions for a pythagorean triplet.

	Args:
		number (int): number to find triplets for

	Returns:
		trips (list): list of all possible pythagorean triplets
	"""	
	
	trips = []
	for a in range(0, number // 3):
		for b in range(a + 1, number // 2):
			c = number - a - b
			if a**2 + b**2 == c**2:
				trips.append([a, b, c])
	return trips


