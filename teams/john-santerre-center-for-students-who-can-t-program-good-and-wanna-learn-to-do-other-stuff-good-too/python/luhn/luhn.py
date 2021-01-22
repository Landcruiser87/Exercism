class Luhn:
	def __init__(self, card_num):
		"""[Initial check's on card number]

		Args:
			card_num ([string]): [Card Number to check]
		"""
		self.card_num = card_num

	def valid(self):
		#Replace blanks spaces
		self.card_num = self.card_num.replace(" ", "")
		
		#Check to see the length of the number is greater than 1
		if len(self.card_num) <= 1:
			return False

		#Check to make sure they're all digits
		if not self.card_num.isdigit():
			return False

		#Reverse the number to start from the right. 
		self.card_num = self.card_num[::-1]
		#List comp to extract the luhn numbers from the even numbers in string
		luhn = sum([int(x)*2 if int(x)*2 < 9 else (int(x)*2 - 9) for x in self.card_num[1::2]])
		#Now sum the odd numbers 
		odd_nums = sum([int(x) for x in self.card_num[0::2]])
		#Put em together and divide by 10 to see if its valid
		luhn = luhn + odd_nums
		return luhn % 10 == 0
