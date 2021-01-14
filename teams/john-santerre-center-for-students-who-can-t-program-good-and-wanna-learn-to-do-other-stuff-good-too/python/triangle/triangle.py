def tri_validate(x):
	"""Decorator function to validate if its a triangle

	Args:
		x ([function]): [pointer for decorator]
	"""

	def inner(sides):
		"""sorts and unpacks the list into individual variables
		Checks to make sure the two smallest sides are longer than the third

		Args:
			sides ([list]): [list of triangle lengths]

		Returns:
			[boolean]: [validated a triangle's basic requirement
			and the decorator function]
		"""

		a, b, c = sorted(sides)
		return a + b > c and x(sides)
	return inner

@tri_validate
def equilateral(sides):
	"""Function to test equilateral triangle.  
	All sides equal meaning when set produces a list of unique values.  
	There should only be one value because its all equal.

	Args:
		sides ([list]): [list of triangle lengths]

	Returns:
		[boolean]: [if length of unique values equal integer for triangle type]
	"""	
	return len(set(sides)) == 1

@tri_validate
def isosceles(sides):
	"""Function to test iscocelese triangle
	2 sides equal.  
	ie - If the count has less than 3 equal sides, Its an iscoceles triangle.
	This works because the tri_validate already makes sure the two smallest sides
	greater than the largest vector in the triangle.

	Args:
		sides ([list]): [list of triangle lengths]

	Returns:
		[boolean]: [if length of unique values equal variable for triangle type]
	"""


	return len(set(sides)) < 3

@tri_validate
def scalene(sides):
	"""Function to test scalene triangle
	If all lengths are different, set will produce 3 values meaning its a scalene tri

	Args:
		sides ([list]): [description]

	Returns:
		[type]: [description]
	"""
	'''
	Args:
		sides ([list]): [list of triangle lengths]
	Returns:
		[boolean]: [if length of unique values equal variable for triangle type]
	'''
	return len(set(sides)) == 3

