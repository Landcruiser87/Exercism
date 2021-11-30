def saddle_points(matrix):
	"""[Finds saddle points in a matrix.  A saddle point is a point in a matrix where the element is greater than or equal to all the elements in its row and less than or equal to all the elements in its column.]

	Args:
		matrix ([List of List of ints]): [Input Matrix to eval]

	Raises:
		ValueError: [If any rows are of different length, raise an error]

	Returns:
		[list of dicts]: [List of dicts with row, column indexes of saddle points]
	"""
	if any([len(row) != len(matrix[0]) for row in matrix]):
		raise ValueError("irregular matrix")

	rowmax = [max(row) for row in matrix]
	colmin = [min(col) for col in zip(*matrix)]

	saddles = []
	for row_idx, row in enumerate(matrix):
		for col_idx, _val in enumerate(row):
			if _val == rowmax[row_idx] and _val == colmin[col_idx]:
				saddles.append({"row":row_idx + 1, "column":col_idx + 1})
	return saddles
