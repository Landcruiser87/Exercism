def leap_year(year:int)->bool:
	"""[leap_year]

	Args:
		year (int): [Year to evaluate]

	Returns:
		bool: [True of False of whether its a leap year]
	"""
	if year % 4 == 0:
		if year % 100 == 0 and year % 400 != 0:
			return False
		else:
			return True
	else:
		return False
	#Rules

	#if year is divisible by 4, its a leap year
	#if year is divisible by 100 it is not a leap year
			#Unless if year is divisible by 400 it is a leap year