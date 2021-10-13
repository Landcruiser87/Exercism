EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

# TODO: define the 'bake_time_remaining()' function
def bake_time_remaining(elapsed_time: int) -> int:
	"""Calculate the bake time remaining.

	:param elapsed_bake_time: int baking time already elapsed.
	:return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'.

	Function that takes the actual minutes the lasagna has been in the oven as
	an argument and returns how many minutes the lasagna still needs to bake
	based on the `EXPECTED_BAKE_TIME`.
	"""
	return EXPECTED_BAKE_TIME - elapsed_time


def preparation_time_in_minutes(number_of_layers):
	"""[summary]

	Args:
		number_of_layers ([int]): [layers o lasagna]

	Returns:
		[int]: [prep time in minutes]
	"""	
	return number_of_layers * PREPARATION_TIME
	
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
	"""[summary]

	Args:
		number_of_layers ([int]): [number of layers of lasagna]
		elapsed_bake_time ([int]): [how long you've been cooking]

	Returns:
		[int]: [prep time(with respect to layers) + elapsed time]
	"""	
	return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time

