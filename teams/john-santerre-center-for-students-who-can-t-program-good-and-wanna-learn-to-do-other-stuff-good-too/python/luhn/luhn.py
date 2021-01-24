class Luhn:
	def __init__(self, card_num):
		"""[Initial check's on card number]

		Args:
			card_num ([string]): [Card Number to check]
		"""
		self.card_num = card_num

	def valid(self):
		self.card_num = self.card_num.replace(" ", "")
		if len(self.card_num) <= 1 or not self.card_num.isdigit():
			return False
		self.card_num = self.card_num[::-1]
		luhn = sum([int(x)*2 if int(x)*2 < 9 else (int(x)*2 - 9) for x in self.card_num[1::2]])
		odd_nums = sum([int(x) for x in self.card_num[0::2]])

		return (luhn + odd_nums) % 10 == 0
