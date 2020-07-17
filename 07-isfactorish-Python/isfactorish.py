# Write the function fun_isfactorish(n) that takes a value int n,
# and returns True if n is a (possibly-negative) integer with exactly 3 unique digits
# (so no two digits are the same), where each of the digits is a factor of the number
# n itself. In all other cases, the function returns False (without crashing).
# For example:
#  assert(fun_isfactorish(412) == True) # 4, 1, and 2 are all factors of 412
#  assert(fun_isfactorish(-412) == True) # Must work for negative numbers!
#  assert(fun_isfactorish(4128) == False) # 4128 has more than 3 digits
#  assert(fun_isfactorish(112) == False) # 112 has duplicate digits (two 1's)
#  assert(fun_isfactorish(420) == False) # 420 has a 0 (0 is not a factor)
#  assert(fun_isfactorish(42) == False) # 42 has a leading 0 (only 2 unique digits)


def fun_isfactorish(n):
	if n < 0:
		 n = -n
	if len(list(set(str(n)))) == 3 and "0" not in str(n):
		for i in str(n):
			if n % int(i) == 0:
				return True
			return False
	return False

