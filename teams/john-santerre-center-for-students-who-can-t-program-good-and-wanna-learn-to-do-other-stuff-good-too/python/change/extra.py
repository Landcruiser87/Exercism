
# from typing import List

# Coins = List[int]


# def find_fewest_coins(coins: Coins, target: int) -> Coins:
#     if target < 0:
#         raise ValueError('Negative change!')

#     # target: (solution size, optimal coin)
#     solutions = {0: (0, None)}

#     for value in range(1, target + 1):
#         for coin in coins:
#             if coin > value:
#                 break
#             if value - coin in solutions:
#                 size, _ = solutions[value - coin]
#                 solutions[value] = min(solutions.get(value, (size + 2,)), (size + 1, coin))

#     if target not in solutions:
#         raise ValueError('Impossible change!')
#     result = []
#     while target:
#         _, coin = solutions[target]
#         result.append(coin)
#         target -= coin
#     return sorted(result)