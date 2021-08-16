def find(search_list, value):
    if len(search_list) == 0:
		raise ValueError("No empty lists allowed")
	
	mid = len(search_list) // 2
	