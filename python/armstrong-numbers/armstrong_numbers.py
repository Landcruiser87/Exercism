def is_armstrong_number(number):
	pow = len(str(number))
	sumz = sum([int(x)**pow for x in str(number)])
	return sumz == number