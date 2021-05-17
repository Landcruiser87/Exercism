from itertools import permutations
from collections import Counter

def find_fewest_coins(coins, target):
	#Get all combinations of coin
	coinCombo = [x for x in permutations(coins,2)]
	
	print(colorCount)

test = find_fewest_coins([1, 5, 10, 25, 100], 15)