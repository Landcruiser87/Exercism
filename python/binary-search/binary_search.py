
def find(search_list, value):
	if len(search_list) == 0:
		raise ValueError("Item not in list or list is empty")
	
	mid_idx = len(search_list) // 2

	if value == search_list[mid_idx]:
		return mid_idx
	elif value < search_list[mid_idx]:
		return find(search_list[:mid_idx], value)
	elif value > search_list[mid_idx]:
		return find(search_list[mid_idx+1:], value) + mid_idx + 1


# def find(search_list, value):
# 	if len(search_list) == 0:
# 		raise ValueError("Item not in list or list is empty")
	
# 	left, right = 0, len(search_list) - 1
# 	while left <= right:
# 		mid_idx = (left + right) // 2
# 		if value == search_list[mid_idx]:
# 			return mid_idx
# 		elif value < search_list[mid_idx]:
# 			right = right - 1
# 		elif value > search_list[mid_idx]:
# 			left = left + 1


# search_list = [1, 3, 4, 6, 8, 9, 11]
# value = 5

# print(find(search_list, value))