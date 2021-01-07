class School:
	'''
	The main utility of this class is to add students names and grades to create a dictionary roster
	'''
	def __init__(self):
		'''
		Initializes empty dict
		Args:
		student = empty dict
		'''
		self.student = {}
		
	def add_student(self, name, grade):
		'''
		Adds the name and grade to the dictionary
		Args:
			name = student name
			grade = grade
		Returns:
			dictionary of student and grade
		'''
		self.student[name] = grade

	def roster(self):
		'''
		Generates a roster for the class from the dictionary above
		Args:
			ros_list = List of students sorted by their name and grade
		Returns: 
			list of sorted student names
		'''
		ros_list = sorted(self.student.items(), key=lambda x:(x[1], x[0]))
		return [item[0] for item in ros_list]

	def grade(self, grade_number):
		'''
		Generates a list of all students in a grade. 
		Args:
			grade_number = The grade of students to return
		Returns:
			list of sorted students in that particular grade.
		'''
		return sorted([name for name, grade in self.student.items() if grade == grade_number])
