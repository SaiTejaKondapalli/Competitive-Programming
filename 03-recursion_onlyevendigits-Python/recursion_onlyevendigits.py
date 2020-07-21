# Without using iteration and without using strings,
# write the recursive function onlyEvenDigits(L),
# that takes a list L of non-negative integers
# (you may assume that), and returns a new list of
# the same numbers only without their odd digits
# (if that leaves no digits, then replace the number with 0).
# So: onlyEvenDigits([43, 23265, 17, 58344]) returns [4, 226, 0, 844].
# Also the function returns the empty list if the original list is empty.
# Remember to not use strings. You may not use loops/iteration in this problem.

def fun_recursion_onlyevendigits(l):
	if len(l) == 0:
		return []
	s = []
	return helper(l, len(l),0, s)

def helper(l, n, i, s):
	if i >= n:
		return s
	d = ""
	for each in str(l[i]):
		if int(each) % 2 == 0:
			d += each
	if len(d) == 0:
		s.append(0)
	else:
		s.append(int(d))
	return helper(l,n,i+1,s)

