# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every
# digit (from 0 to 9) at least once. 309 is the smallest number with this property.
# Write the function nthWithProperty309 that takes a non-negative int n and returns
# the nth number with Property309.

def nthwithproperty309(n):
	# Your code goes here
	count = 0
	i = 309
	while True:
		l = "".join(sorted(list(str(i ** 5))))
		if "0123456789" in l:
			if count == n:
				return i
			count += 1
		i += 1