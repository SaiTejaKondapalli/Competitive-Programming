# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
	# your code goes here
	s = str(abs(n))
	if len(s) == 1:
		return False
	for i in range(1,len(s)):
		if s[i] == s[i - 1]:
			return True
	return False

