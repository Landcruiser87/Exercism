# def find(search_list, value):
# 	if len(search_list) == 0:
# 		raise ValueError("No empty lists allowed!!")
	
# 	mid_idx = len(search_list) // 2

# 	if value == search_list[mid_idx]:
# 		return mid_idx
# 	elif value < search_list[mid_idx]:
# 		return find(search_list[:mid_idx], value)
# 	elif value > search_list[mid_idx]:
# 		return find(search_list[mid_idx+1:], value) + mid_idx + 1


def find(search_list, value):
	if len(search_list) == 0:
		raise ValueError("No empty lists allowed!!")
	
	mid_idx = len(search_list) // 2
	
	if value == search_list[mid_idx]:
		return mid_idx
	elif value < search_list[mid_idx]:
		return find(search_list[:mid_idx], value)
	elif value > search_list[mid_idx]:
		return find(search_list[mid_idx+1:], value) + mid_idx + 1





# search_list = [1, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 634]
# value = 144

# print(find(search_list, value))
