import os
def square(number):
	if not 0 < number < 65:
		raise ValueError("Number must be between 0 and 64")
	return 2**(number-1)

def total():
	return 2**64 - 1
