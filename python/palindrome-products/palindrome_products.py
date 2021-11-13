def largest(min_factor, max_factor):
	"""Given a range of numbers, find the largest palindromes which
	   are products of two numbers within that range.

	:param min_factor: int with a default value of 0
	:param max_factor: int
	:return: tuple of (palindrome, iterable).
			 Iterable should contain both factors of the palindrome in an arbitrary order.
	"""  
	result = product_piler(min_factor, max_factor)
	if len(result) == 0:
		return (None, [])
	else:
		return (result[-1][0],[sorted(res[1]) for res in result if res[0]==result[-1][0]])
		
def smallest(min_factor, max_factor):
	"""Given a range of numbers, find the smallest palindromes which
	are products of two numbers within that range.

	:param min_factor: int with a default value of 0
	:param max_factor: int
	:return: tuple of (palindrome, iterable).
	Iterable should contain both factors of the palindrome in an arbitrary order.
	"""
	result = product_piler(min_factor, max_factor)
	if len(result) == 0:
		return (None, [])
	else:
		return (result[0][0],[sorted(res[1]) for res in result if res[0]==result[0][0]])

def product_piler(min_factor:int, max_factor:int)->dict:
	"""[compiles a list of all palindromes within a range of numbers]

	Args:
		min_factor (int): [min of range]
		max_factor (int): [max of range]

	Returns:
		list: [tuple of value and composite factors to reach value]
	"""	
	if min_factor > max_factor:
		raise ValueError("min must be <= max")

	res = []
	for x in range(min_factor, max_factor + 1):
		for y in range(min_factor, max_factor + 1):
			num = x*y
			if is_palindrome(num):
				res.append((num, [x, y]))
	return sorted(res, key=lambda x: x[0])
	
def is_palindrome(num:int)->bool:
	"""[Checks if number is palindrome]

	Args:
		num (int): [product of numbers]

	Returns:
		bool: [Whether its a palindrome]
	"""	
	if str(num) == str(num)[::-1]:
		return True
	else:
		return False
