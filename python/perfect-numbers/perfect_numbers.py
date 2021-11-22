def classify(number):
	""" A perfect number equals the sum of its positive divisors.

	:param number: int a positive integer
	:return: str the classification of the input integer
	"""
	if number <= 0:
		raise ValueError("Classification is only possible for positive integers.")

	sum_of_the_facts = sum([x for x in range(1, number) if number % x == 0])
	
	if sum_of_the_facts == number:
		return "perfect"
	elif sum_of_the_facts > number:
		return "abundant"
	elif sum_of_the_facts < number:
		return "deficient"

