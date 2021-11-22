import string
class PhoneNumber(object):
	def __init__(self, p_number):

		self.number = self.clean_num(p_number)
		self.area_code = self.number[:3]
		self.the_rest = self.number[-7:]
		self.check_therest()

	def clean_num(self, number):
		self.check_it_punc(number)
		self.check_it_alpha(number)
		clean = "".join(x for x in number if x.isdigit())
		if len(clean) < 10:
			raise ValueError("incorrect number of digits")
		if len(clean) > 11:
			raise ValueError("more than 11 digits")
		if len(clean) == 10:
			return clean
		if len(clean) == 11 and clean[0] == '1':
			return clean[1:]	
		if len(clean) == 11 and clean[0] != '1':
			raise ValueError("11 digits must start with 1")
	
	def check_it_punc(self, number):
		_oklist = ['(', ')', '-', ' ', '.', '+']
		if any(item in number for item in string.punctuation if item not in _oklist):
			raise ValueError("punctuations not permitted")

	def check_it_alpha(self, number):
		if any(item.isalpha() for item in number):
			raise ValueError("letters not permitted")

	def check_therest(self):
		if self.area_code[0] == '0':
			raise ValueError("area code cannot start with zero")
		if self.area_code[0] == '1':
			raise ValueError("area code cannot start with one")
		if self.the_rest[0] == '0':
			raise ValueError("exchange code cannot start with zero")
		if self.the_rest[0] == '1':
			raise ValueError("exchange code cannot start with one")		
		return True

	def pretty(self):
		return f"({self.area_code})-{self.the_rest[:3]}-{self.the_rest[-4:]}"
