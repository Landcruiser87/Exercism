
def find(search_list, value):
	"""[finding things]

	Args:
		search_list ([list]): [list of sorted int values]
		value ([int]): [Value we're lookin for]

	Raises:
		ValueError: [If it doesn't find the value, hello error]

	Returns:
		[int]: [index of value in search_list]
	"""
	if len(search_list) == 0:
		raise ValueError("Item not in list or list is empty")
	
	mid_idx = len(search_list) // 2

	if value == search_list[mid_idx]:
		return mid_idx
	elif value < search_list[mid_idx]:
		return find(search_list[:mid_idx], value)
	elif value > search_list[mid_idx]:
		return find(search_list[mid_idx+1:], value) + mid_idx + 1
