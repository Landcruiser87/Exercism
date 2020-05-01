def is_isogram(string):
	string = [x for x in string.lower() if x.isalpha()]
	return len(string) == len(set(string))
