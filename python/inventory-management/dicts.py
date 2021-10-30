def create_inventory(items):
	"""

	:param items: list - list of items to create an inventory from.
	:return:  dict - the inventory dictionary.
	"""

	return {x:items.count(x) for x in items}


def add_items(inventory, items):
	"""

	:param inventory: dict - dictionary of existing inventory.
	:param items: list - list of items to update the inventory with.
	:return:  dict - the inventory dictionary update with the new items.
	"""
	for item in items:
		if item not in inventory:
			inventory[item] = 1
		else:
			inventory[item] += 1
	
	return inventory


def decrement_items(inventory, items):
	"""

	:param inventory: dict - inventory dictionary.
	:param items: list - list of items to decrement from the inventory.
	:return:  dict - updated inventory dictionary with items decremented.
	"""
	for item in items:
		if inventory[item] > 0:
			inventory[item] -= 1
	return inventory

	# return {k:v-items.count(k) for k,v in inventory.items() if v > 0 and k in items}
	
	
def remove_item(inventory, item):
	"""
	:param inventory: dict - inventory dictionary.
	:param item: str - item to remove from the inventory.
	:return:  dict - updated inventory dictionary with item removed.
	"""
	if item in inventory:
		inventory.pop(item)
	return inventory

def list_inventory(inventory):
	"""

	:param inventory: dict - an inventory dictionary.
	:return: list of tuples - list of key, value pairs from the inventory dictionary.
	"""

	return [(k, v) for k, v in inventory.items() if v > 0]
