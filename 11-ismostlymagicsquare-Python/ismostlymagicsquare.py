# isMostlyMagicSquare(a) [15 pts]
# Write the function isMostlyMagicSquare(a) that takes an 2d list of numbers, which you may assume is an NxN square
# with N>0, and returns True if it is "mostly magic" and False otherwise, where a square is "mostly magic" if:
# Each row, each column, and each of the 2 diagonals each sum to the same total.
# A completely magic square has additional restrictions (such as not allowing duplicates, and only allowing numbers
# from 1 to N2), which we are not enforcing here, but which you can read about here. Note: any magic square is also
# a "mostly magic" square, including this sample magic square:
# Read for more: https://en.wikipedia.org/wiki/Magic_square
# Here is another mostly-magic square:
# [ [ 42 ]]
# That square is 1x1 and each row, column, and diagonal sums to 42! And finally, here is a not-mostly-magic square:
# [ [ 1, 2],
#   [ 2, 1]]
# Each row and each column add to 3, but one diagonal adds to 2 and the other to 4.

def ismostlymagicsquare(a):
	# Your code goes here
	rowsum = list(map(sum, a))
	if len(list(set(rowsum))) == 1:
		rowsum = rowsum[0]
	else:
		return False
	print(rowsum)
	colsum = []
	summ = 0
	for i in range(len(a)):
		for j in range(len(a[0])):
			summ += a[j][i]
		colsum.append(summ)
		summ = 0
	if len(list(set(colsum))) == 1:
		colsum = colsum[0]
	else:
		return False
	print(colsum)
	if rowsum != colsum:
		return False
	diag1 = 0
	diag2 = 0
	for i in range(len(a)):
		for j in range(len(a[0])):
			if i == j:
				diag1 += a[i][j]
			if (i + j) == len(a) - 1:
				diag2 += a[i][j]
	print(diag1,diag2)
	if diag1 != diag2:
		return False
	else:
		if rowsum == colsum == diag1 == diag2:
			return True
		return False



