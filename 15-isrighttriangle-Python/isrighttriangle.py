# isrighttriangle(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function isrighttriangle(x1, y1, x2, y2, x3, y3) that takes 6 int or float values that
# represent the vertices (x1,y1), (x2,y2), and (x3,y3) of a triangle, and returns True if that is
# a right triangle and False otherwise. You may wish to write a helper function,
# distance(x1, y1, x2, y2), which you might call several times. Also, remember to use
# almostEqual (instead of ==) when comparing floats.
import math
def isrighttriangle(x1, y1, x2, y2, x3, y3):
	# your code goes here
	d1 = distance(x1, y1, x2, y2)
	d2 = distance(x2, y2, x3, y3)
	d3 = distance(x3, y3, x1, y1)
	x, y, z = sorted([d1, d2, d3])
	print(x ** 2 + y ** 2)
	print(z ** 2)
	if math.isclose(x ** 2 + y ** 2, z ** 2):
		return True
	return False

def distance(x1, y1, x2, y2):
	return math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2))