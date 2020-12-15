class Garden():
'''
Returns plant's position on thie window sill
Set up Global vars for plant_dic and students
'''

	plant_dic = {
				"C": "Clover",
				"G": "Grass",
				"R": "Radishes",
				"V": "Violets"}

	students = ['Alice','Bob','Charlie','David',
					'Eve','Fred','Ginny','Harriet',
					'Ileana','Joseph','Kincaid','Larry']

	def __init__(self, diagram, students=students):
		'''
		Split the string
		Sorts students
		Calls plant function to get plant name for student
		'''
		self.diagram = diagram.splitlines()
		self.students = sorted(students)
		self.plants(diagram, students)

	def plants(self,diagram, students):
		'''
		unpacks students
		Determines start and end position of student
		Joins the rows of data
		Looks up the plants used by student. 
		returns plant names.
		'''
		for x, student in enumerate(students):
			start = 2 * x
			end = start + 2
			plants = ''.join(row[start:end] for row in diagram)
			return [self.plant_dic[p] for p in plants]
		
		

		#Takes in student name
		#returns a list of plnats that student has planted. 


import unittest


class KindergartenGardenTest(unittest.TestCase):
	def test_partial_garden_garden_with_single_student(self):
		garden = Garden("RC\nGG")
		self.assertEqual(
			garden.plants("Alice"), ["Radishes", "Clover", "Grass", "Grass"]
		)

	def test_partial_garden_different_garden_with_single_student(self):
		garden = Garden("VC\nRC")
		self.assertEqual(
			garden.plants("Alice"), ["Violets", "Clover", "Radishes", "Clover"]
		)

	def test_partial_garden_garden_with_two_students(self):
		garden = Garden("VVCG\nVVRC")
		self.assertEqual(
			garden.plants("Bob"), ["Clover", "Grass", "Radishes", "Clover"]
		)

if __name__ == "__main__":
	unittest.main()
