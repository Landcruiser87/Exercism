import math
def triplets_with_sum(number:int) -> list:
	"""This is a brute force approach for calculating all the combinations 
	that satisfy the conditions for a pythagorean triplet.

	Args:
		number (int): number to find triplets for

	Returns:
		trips (list): list of all possible pythagorean triplets
	"""	
	
	trips = []
	for a in range(1, number//3):
		b = (number/2)*(2*a-number)/(a-number)
		c = math.sqrt(a**2 + b**2)
		if b.is_integer() and c.is_integer() and 0<a<b<c<number:
			trips.append([a, int(b), int(c)])
	return trips
