from collections import Counter

def find_anagrams(word:str, candidates:list)->list:
	"""[List comprehension to find anagrams]

	Args:
		word (str): [Word to compare]
		candidates (list): [List of possible matches]

	Returns:
		list: [Any candidate from candidate list
		if the function is_anagram returns True]
	"""	
	return [cand for cand in candidates if is_anagram(word, cand)]

def is_anagram(word:str, candidate:str)->bool:
	"""[Determines if word is anagram.
	If word not equal to candidate and 
	A counter object of each str are equal]

	Args:
		word (str): [Input word lowered]
		candidate (str): [Single comparison word lowered]

	Returns:
		bool: [Result of two gates]
	"""	
	return word.lower() != candidate.lower() and Counter(word.lower()) == Counter(candidate.lower()) 