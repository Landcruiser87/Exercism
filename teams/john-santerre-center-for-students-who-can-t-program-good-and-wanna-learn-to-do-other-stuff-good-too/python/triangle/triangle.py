def tri_validate(x):
	'''
	Decorator function to validate if its a triangle
	'''
	def inner(sides):
		'''
		sorts and unpacks the list into individual variables
		Checks to make sure the two smallest sides are longer than the third
		Args:
			sides = List of tri lengths
			a, b, c = Individual tri length components
			x = returns the decorator function to correct function that called it
		Returns:
			boolean validating a triangle's basic requirement and the decorator function.
		'''
		a, b, c = sorted(sides)
		return a + b > c #and x(sides)
	return inner

@tri_validate
def equilateral(sides):
	'''
	Function to test equilateral triangle. 
	All sides equal meaning when set produces a list of unique values.  
	There should only be one value because its all equal.
	
	Args:
		sides = List of triangle lengths
	Returns:
		Boolean of if length of unique values equal variable for triangle type
	'''
	return len(set(sides)) == 1

@tri_validate
def isosceles(sides):
	'''Function to test iscocelese triangle
	2 sides equal.  
	ie - If the count has less than 3 equal sides, Its an iscoceles triangle.
	This works because the tri_validate already makes sure the two smallest sides
	greater than the largest vector in the triangle.
	
	Args:
		sides = List of triangle lengths
	Returns:
		Boolean of if length of unique values equal variable for triangle type
	'''

	return len(set(sides)) < 3

@tri_validate
def scalene(sides):
	'''
	Function to test scalene triangle
	If all lengths are different, set will produce 3 values meaning its a scalene tri

	Args:
		sides = List of triangle lengths
	Returns:
		Boolean of if length of unique values equal variable for triangle type
	'''
	return len(set(sides)) == 3


import unittest

class EquilateralTriangleTest(unittest.TestCase):
    def test_all_sides_are_equal(self):
        self.assertIs(equilateral([2, 2, 2]), True)

    def test_any_side_is_unequal(self):
        self.assertIs(equilateral([2, 3, 2]), False)

    def test_no_sides_are_equal(self):
        self.assertIs(equilateral([5, 4, 6]), False)

    def test_all_zero_sides_is_not_a_triangle(self):
        self.assertIs(equilateral([0, 0, 0]), False)

    def test_sides_may_be_floats(self):
        self.assertIs(equilateral([0.5, 0.5, 0.5]), True)


class IsoscelesTriangleTest(unittest.TestCase):
    def test_last_two_sides_are_equal(self):
        self.assertIs(isosceles([3, 4, 4]), True)

    def test_first_two_sides_are_equal(self):
        self.assertIs(isosceles([4, 4, 3]), True)

    def test_first_and_last_sides_are_equal(self):
        self.assertIs(isosceles([4, 3, 4]), True)

    def test_equilateral_triangles_are_also_isosceles(self):
        self.assertIs(isosceles([4, 4, 4]), True)

    def test_no_sides_are_equal(self):
        self.assertIs(isosceles([2, 3, 4]), False)

    def test_first_triangle_inequality_violation(self):
        self.assertIs(isosceles([1, 1, 3]), False)

    def test_second_triangle_inequality_violation(self):
        self.assertIs(isosceles([1, 3, 1]), False)

    def test_third_triangle_inequality_violation(self):
        self.assertIs(isosceles([3, 1, 1]), False)

    def test_sides_may_be_floats(self):
        self.assertIs(isosceles([0.5, 0.4, 0.5]), True)


class ScaleneTriangleTest(unittest.TestCase):
    def test_no_sides_are_equal(self):
        self.assertIs(scalene([5, 4, 6]), True)

    def test_all_sides_are_equal(self):
        self.assertIs(scalene([4, 4, 4]), False)

    def test_two_sides_are_equal(self):
        self.assertIs(scalene([4, 4, 3]), False)

    def test_may_not_violate_triangle_inequality(self):
        self.assertIs(scalene([7, 3, 2]), False)

    def test_sides_may_be_floats(self):
        self.assertIs(scalene([0.5, 0.4, 0.6]), True)


if __name__ == "__main__":
    unittest.main()

	