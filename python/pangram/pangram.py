import string

def is_pangram(sentence):
	alphb = string.ascii_lowercase
	return set(alphb) <= set(sentence.lower())

