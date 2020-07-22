# longestDigitRun(n) [20 pts]
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and returns
# the digit that has the longest consecutive
# run, or the smallest such digit if there is a tie. So, longestDigitRun(117773732) returns 7 (
# because there is a run of 3 consecutive 7's),
# as does longestDigitRun(-677886).
def longestdigitrun(n):
	# Your code goes here
	s = str(abs(n))
	res = s[0]
	count = 0
	m = []
	for i in range(len(s)):
		c = 1
		for j in range(i + 1, len(s)):
			if s[i] != s[j]:
				break
			c += 1
		if c >= count:
			if c == count:
				count = c
				m.append(s[i])
				res = min(s[i], min(m))
			else:
				count = c
				res = s[i]
	return int(res)