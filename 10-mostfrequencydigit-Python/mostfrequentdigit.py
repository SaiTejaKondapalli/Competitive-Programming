# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
	# your code goes here
	# return int(max(set(list(str(n))),key = list(str(n)).count))
	maximum = 0
	res = str(n)[0]
	for i in str(n):
		if count(i) > maximum:
			maximum = count(i)
			res = i
	return int(res)
