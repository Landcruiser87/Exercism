#%%
from itertools import combinations as cb

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
DISCOUNT = [0, 0.05, 0.10, 0.15, 0.2, 0.25]

def total(basket:list) -> int:
	_bk_cnt = len(basket)
	_unq_bk_cnt = len(set(basket))	

	groups = []
	#need a function that can find out the other groupings with CWR
	for x in range(1, _unq_bk_cnt):
		for bsk_1 in cb(basket, x):

			if sum(bsk_1) == _bk_cnt:
				bsk_1 = list(bsk_1)
				bsk_2 = basket.copy()
				
				for item in bsk_1:
					bsk_2.remove(item)
				
				bsk_sum = calc_basket(bsk_1) + calc_basket_remain(bsk_2)
				#remove that set from the basket into two lists. 
				#calculate the price of both lists and add to sums list

				groups.append(int(bsk_sum))

	return min(groups)

def calc_basket(bsk:list) -> int:
	a = list(set(bsk))
	b = bsk.copy()

	for item in a:
		b.remove(item)
	
	a_total = PRICES[len(a)] - PRICES[len(a)]*DISCOUNT[len(a)-1]
	b_total = PRICES[len(b)]

	bsk_sum = a_total + b_total
	
	#If Different books.  Apply discount to any unique book
	#if multiple of same book exist (with a separate book)
	
	return bsk_sum

def calc_basket_remain(bsk:list) -> int:
	_counts = {i:bsk.count(i) for i in bsk}
	bsk_total = [PRICES[j] for j in _counts.values()]
	return sum(bsk_total)


# basket =  [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]  #6000
# print(total(basket))



#%%
# _bk_cnt = len(basket)
# _unq_bk_cnt = len(set(basket))	
# _counts = {i:basket.count(i) for i in basket}

# book_sets = [set() for value in range(0, max(_counts.values()))]
# for key, value in _counts.items():
# 	for index in range(0, value):
# 		book_sets[index].add(key)
