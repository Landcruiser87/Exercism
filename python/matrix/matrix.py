class Matrix:
	def __init__(self, matrix_string):
		matrix = [row.split(' ') for row in matrix_string.splitlines()]
		self.matrix = [[int(s) for s in row] for row in matrix]
		
	def row(self, index):
		return self.matrix[index-1]

	def column(self, index):
		return [row[index-1] for row in self.matrix]
