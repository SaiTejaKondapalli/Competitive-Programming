# Write the function fun_nth_palindromic_prime(n) that takes a non-negative int n
# and returns the nth palindromic Prime, which is a palidrome number such that
# it is also a prime. For example, 313 is a palindrome and it is prime
# so 313 is an palindrome Prime. fun_nth_palindrome_prime(0) returns 2


def isprime(n):
	count = 0
	for i in range(1, n + 1):
		if n % i == 0:
			count +=1
	return count == 2
def ispalindrome(n):
	# return n[::-1] == n
	temp = n
	rev = 0
	while n > 0:
		rev = rev * 10 + n % 10
		n = n // 10
	return rev == n
def fun_nth_palindromic_prime(n):
	count = 0
	i = 0
	while True:
		if isprime(i) and ispalindrome(i):
			if count == n:
				return i
			count += 1
		i += 1