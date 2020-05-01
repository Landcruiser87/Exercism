import string
import re

def strip_punc(my_string):
	'''
	Removes punctuation from the string
	replaces , and _ with a space
	if a word is surrounded in quotes, it replaces the word in the string without them
	then checks each character to remove punctuation if its in the punct_list
	'''
	punct_list = set('''!:@$%^&.\n''')
	my_string.splitlines()

	my_string = ' '.join(my_string.split(','))
	my_string = ' '.join(my_string.split('_'))
	for word in my_string.split():
		if word.startswith("'") and word.endswith("'"):
			my_string = my_string.replace(word, word.strip("'"))
	
	cleaned = ''.join(ch for ch in my_string if ch not in punct_list)
	return cleaned

def count_words(sentence):
	'''
	lowers and splits every string
	Checks if its in the dictionary keys and adds count accordingly
	'''
	dic = dict()
	sentence = strip_punc(sentence)
	for x in sentence.lower().split():
		if x in dic.keys():
			dic[x] = dic[x] + 1
		else:
			dic[x] = 1
	return dic

