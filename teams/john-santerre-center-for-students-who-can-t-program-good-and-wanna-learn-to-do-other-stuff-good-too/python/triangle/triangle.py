def tri_validate(x):
	'''
	Function to validate if its a triangle
	'''
	def inner(sides):
		'''

		'''
		a, b, c = sorted(sides)
		return a + b > c and x(sides)
	return inner

@tri_validate
def equilateral(sides):
	'''
	Function to test equilateral triangle. 
	All sides equal


	'''
	return len(set(sides)) == 1

@tri_validate
def isosceles(sides):
	'''Function to test iscocelese triangle
	2 sides equal
	'''
	return len(set(sides)) < 3

@tri_validate
def scalene(sides):
	return len(set(sides)) == 3