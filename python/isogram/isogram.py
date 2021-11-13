def is_isogram(string):
	string = [x.lower() for x in string if x.isalpha()]
	return len(string) == len(set(string))
