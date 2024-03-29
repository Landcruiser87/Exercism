def find(search_list:list, value:int)->int:
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
	
	left, right = 0, len(search_list) - 1
	while left <= right:
		mid_idx = (left + right) // 2
		if value == search_list[mid_idx]:
			return mid_idx
		elif value < search_list[mid_idx]:
			right = right - 1
		elif value > search_list[mid_idx]:
			left = left + 1
