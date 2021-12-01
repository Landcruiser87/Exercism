def factors(value: int) -> list:
	"""[Prime Factor Finder]

	Args:
		value ([int]): [Input value to find prime factors]

	Returns:
		[list]: [List of possible prime factors]
	"""
	factors = []
	i = 2

	while i - 1 < value:
		while value % i == 0:
			factors.append(i)
			value = value / i
		i += 1			
	return factors
