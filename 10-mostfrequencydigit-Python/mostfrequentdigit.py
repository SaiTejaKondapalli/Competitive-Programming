# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
	# your code goes here
	# return int(max(set(list(str(n))),key = list(str(n)).count))
	d = {}
	for i in str(n):
		if i not in d:
			d[i] = count(i)
	maximum = max(d.values())
	l = []
	for i in d:
		if d[i] == maximum:
			l.append(i)
	return min(l)
