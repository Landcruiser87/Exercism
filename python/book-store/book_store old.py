#%%
from itertools import combinations as cb
#! Ditched this path because the combinations kept failing 
#! edge cases as well as just being janky in general. 



#GlobalVars
#BasePrice
B_PRICE = 800
#Price Dictionary
PRICES = {
		  0:0,
		  1:B_PRICE,
		  2:B_PRICE*2,
		  3:B_PRICE*3,
		  4:B_PRICE*4,
		  5:B_PRICE*5,
		}
DISCOUNT = [0, 0.05, 0.10, 0.2, 0.25]

def total(basket:list) -> int:
	if not bool(basket):
		return 0
	_unq_bk_cnt = len(set(basket))

	groups = []
	for x in range(1, len(basket)+1):
		for bsk_1 in cb(basket, x):
			bsk_1 = list(bsk_1)
			bsk_2 = basket.copy()
			
			for item in bsk_1:
				bsk_2.remove(item)
			
			# if bsk_1 == [1,2,3,4,5]:
			# 	print("hit it")
			bsk_sum = calc_basket(bsk_1) + calc_basket(bsk_2)
			groups.append(int(bsk_sum))

	return min(groups)

def calc_basket(bsk:list) -> int:
	a = list(set(bsk))
	
	for item in a:
		bsk.remove(item)
	
	a_total = PRICES[len(a)] - PRICES[len(a)]*DISCOUNT[len(a)-1]
	b_total = PRICES[len(bsk)]

	bsk_sum = a_total + b_total

	return bsk_sum

# #Old function for calculating the back half of a split basket.
# def calc_basket_remain(bsk:list) -> int:
# 	_counts = {i:bsk.count(i) for i in bsk}
# 	bsk_total = [PRICES[j] for j in _counts.values()]
# 	return sum(bsk_total)


# basket =  [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]  #6000
# # basket =  [1, 1, 2, 2, 3, 3, 4, 5]  #5120
# basket = [1, 1, 2, 2, 3, 3, 4, 5, 1, 1, 2, 2, 3, 3, 4, 5] #10240
# # basket = []

# print(total(basket))
