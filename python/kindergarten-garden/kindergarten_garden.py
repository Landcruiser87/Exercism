class Garden:
'''
Define the plant dictionary for reference to placement chart.
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
        self.diagram = diagram.splitlines("/n")
		self.students = students

	def plants(self,students):
		student_names = sorted([x[0] for x in self.students])
		

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



# "C:\Program Files (x86)\Microsoft Office\root\Office16\MSACCESS.EXE" "C:\Users\andyh\Google Drive\Job\UpWork\Cleveland\OldVersion\Cleveland Golf R&D Database.mdb" /WRKGRP "C:\Users\andyh\Google Drive\Job\UpWork\Cleveland\OldVersion\Secured.mdw"



#   right:
#     - icon: fa-envelope fa-lg
#       href: contact.html
#     - icon: fa-github fa-lg
#       href: https://github.com/Landcruiser87
#     - icon: <i class="fab fa-linkedin-in"></i>
#       href: https://www.linkedin.com/in/data-science-and/y