def is_paired(input_string:str)-> bool:
	"""Program for traversing an input string to check for 
	proper bracket ordering and pairing. 

	Args:
		input_string (str): random string of brackets

	Returns:
		bool: True if brackets are properly paired, False otherwise
	"""	

	brac_list = ['(', ')', '[', ']', '{', '}']
	brac_dict = {
			')':'(', 
			'}':'{', 
			']':'['}
	
	#Get rid of anything thats not a bracket.
	filter_input = "".join([x for x in input_string if x in brac_list])
	#Attempted to use Counter() to count the number of each bracket types
	#Doesn't track order though
	# counts = Counter(filter_input)
	# for key in brac_dict:
	# 	if counts[key] != counts[brac_dict[key]]:
	# 		return False

	#Empty list container for an ordered list
	brac_stack = [] 

	#Iterate through the string
	for char in filter_input:
		#Check if current char is an opening
		if char in brac_dict.values():
			brac_stack.append(char)
		
		#Check if current char is an closing
		if char in brac_dict.keys():
			#If stack is empty, return False
			if not brac_stack:
				return False
			
			#Check latest item in stack against its corresponding closing in brac_dict
			#If they don't match, return False
			if brac_stack.pop() != brac_dict[char]:
				return False
			
			#Keep iterating through the string
			else:
				continue
	
	#If stack is empty, its a valid bracket pairing
	if not brac_stack:
		return True
	else:
		return False		
		