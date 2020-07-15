# Write the function nearestOdd(n) that takes an float n,
# and returns as an int value the nearest odd number to n.
# In the case of a tie, return the smaller odd value.
# Note that the result must be an int, so nearestOdd(13.0) is the int 13, and not the float 13.0.


import numpy
def fun_nearestodd(n):
	if int(n) % 2 == 1:
			return int(n)
	if (n / 2) % 2 == 0:
		return int(numpy.floor(n) // 2 * 2 - 1)
	else:
		return int(numpy.ceil(n) // 2 * 2 + 1)


