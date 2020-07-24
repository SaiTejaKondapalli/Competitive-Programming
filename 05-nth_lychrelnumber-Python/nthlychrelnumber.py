# nthLychrelNumber(n) [20 pts]
# A Lychrel number is a natural number that cannot form a palindrome through the iterative process of
# repeatedly reversing its digits and adding the resulting numbers. This process is sometimes called the
# 196-algorithm, after the most famous number associated with the process.
# The first few Lychrel numbers are 196, 295, 394, 493, 592, 689, 691, 788, 790, 879, 887….
def reverse(n):
	rev = 0
	while n != 0:
		rev = rev * 10 + n % 10
		n = n // 10
	return rev
def ispalindrome(n):
	return n == reverse(n)
def islychrel(n):
	for i in range(500):
		n = n + reverse(n)
		if ispalindrome(n):
			return False
	return True
def nthlychrelnumbers(n):
	# your code goes here
	i = 1
	count = 0
	while True:
		if islychrel(i):
			count += 1
			if count == n:
				return i
		i+=1
