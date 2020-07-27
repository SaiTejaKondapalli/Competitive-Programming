# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every
# digit (from 0 to 9) at least once. 309 is the smallest number with this property.
# Write the function nthWithProperty309 that takes a non-negative int n and returns
# the nth number with Property309.

def nthwithproperty309(n):
	# Your code goes here
	if n == 0:
		return 309
	count = 0
	i = 310
	while True:
		l = str(pow(i,5))
		# if "0" in l and "1" in l and "2" in l and "3" in l and "4" in l and "5" in l and "6" in l and "7" in l and "8" in l and "9" in l:
		if "[0-9]" in l:
			count += 1
			if count == n:
				return i
		i += 1