class Garden():
# '''
# Define the plant dictionary and student list for reference to placement chart.

# First splits the diagram into 2 rows
# Sorts the students alphabetically (As that is how they're assigned)
# '''
plant_dic = {
		"C": "Clover",
		"G": "Grass",
		"R": "Radishes",
		"V": "Violets"}

students = ['Alice','Bob','Charlie','David',
				'Eve','Fred','Ginny','Harriet',
				'Ileana','Joseph','Kincaid','Larry']

	def __init__(self, diagram, students=students):
		self.diagram = diagram.splitlines("/n")
		self.students = sorted(students)
		self.plants(diagram, students)

	def plants(self,diagram, students):
		for x, student in enumerate(students)
			start = 2 * x
			end = start + 2
			plants = ''.join(row[start:end] for row in diagram)
			self.student = [self.plant_dic[p] for p in plants]
		
		

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



