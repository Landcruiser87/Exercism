#

def is_valid(isbn:str)->bool:
	isbn = isbn.replace('-', '')
	if len(isbn) != 10:
		return False
	isbn = list(isbn)

	if isbn[-1] == "X":
		isbn[-1] = "10"
	for x in isbn:
		if x.isdigit() == False:
			return False
	return sum(int(i) * (10 - j) for j, i in enumerate(isbn)) % 11 == 0