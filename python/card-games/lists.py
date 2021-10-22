import os
def get_rounds(number):
	"""

	 :param number: int - current round number.
	 :return: list - current round and the two that follow.
	"""

	return list([number, number + 1, number + 2])


def concatenate_rounds(rounds_1, rounds_2):
	"""

	:param rounds_1: list - first rounds played.
	:param rounds_2: list - second set of rounds played.
	:return: list - all rounds played.
	"""

	return rounds_1 + rounds_2


def list_contains_round(rounds, number):
	"""

	:param rounds: list - rounds played.
	:param number: int - round number.
	:return:  bool - was the round played?
	"""

	return number in rounds


def card_average(hand):
	"""

	:param hand: list - cards in hand.
	:return:  float - average value of the cards in the hand.
	"""

	return sum(hand)/len(hand)


def approx_average_is_average(hand):
	"""

	:param hand: list - cards in hand.
	:return: bool - is approximate average the same as true average?
	"""

	app_avg = (hand[0] + hand[-1])/2
	median = sorted(hand)[len(hand)//2]
	if median == sum(hand)/len(hand):
		return True
	elif app_avg == card_average(hand):
		return True
	else:
		return False


def average_even_is_average_odd(hand):
	"""

	:param hand: list - cards in hand.
	:return: bool - are even and odd averages equal?
	"""
	odd_avg = sum(hand[1::2])/len(hand[1::2])
	even_avg = sum(hand[::2])/len(hand[::2])
	if even_avg == odd_avg:
		return True
	else:
		return False

def maybe_double_last(hand):
	"""

	:param hand: list - cards in hand.
	:return: list - hand with Jacks (if present) value doubled.
	"""

	if hand[-1] == 11:
		return hand[:-1] + [22]
	else:
		return hand
		
