from itertools import combinations_with_replacement as cwr


def find_fewest_coins(coins:list, target:int)-> list:
	"""[Function to find the fewest coins in change]

	Args:
		coins ([list]): [List of the coins available]
		target ([int]): [Value of which change is made]

	Raises:
		ValueError: [Target input is less than change]
		ValueError: [Couldn't get the proper amount in coins]

	Returns:
		[list]: [List of coins for appropriate change]
	"""	
	if target == 0:
		return []
	if target < min(coins):
		raise ValueError("Somethins whack with your target")

	# iterate up to target value divided by the minimum coin
	# Seeing as at the very least you'd use all of that min coin
	# to reach the target value.  
	# From those coins generate combinations with replacement
	# ie - all possible coin combinations with the coins available
	# If the sum is == to the target.  You've got the mininum coins~!
	
	for i in range(1, target // min(coins) + 1):
		for c in cwr(coins, i):
			if sum(c) == target:
				return list(c)
	
	raise ValueError("No entiendo!  Change not possible!")
