class Garden():
	'''
	Takes in student name
	returns a list of plants that student has planted. 
	First assigns plant dictionary and student list as global vars
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
		Split the input string
		Sorts students
		'''
		self.diagram = diagram.splitlines()
		self.students = sorted(students)

	def plants(self, student):
		''' 
		finds the index of the student
		Joins the rows of data
		Looks up the plants used by student. 
		returns plant names.
		'''
		x = self.students.index(student)
		plants = ''.join(row[2*x:2*x+2] for row in self.diagram)
		return [self.plant_dic[p] for p in plants]
