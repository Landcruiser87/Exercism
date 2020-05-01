vec = [-8, -4, -2, 2, 4, 8]

[x for x in vec if vec >= 0]

[abs(x) for x in vec]

[x**2 for x in vec]

[(x, x**2) for x in vec]

from math import pi
[str(round(pi, i)) for i in range(1,6)]

matrix = [
	[1, 2, 3, 4],
	[5, 6, 7, 8],
	[9, 10, 11, 12],
]

list(zip(*matrix))