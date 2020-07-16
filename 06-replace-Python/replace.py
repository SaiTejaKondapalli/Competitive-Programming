# Without using the builtin method s.replace(),
# write its equivalent. Specifically, write the function
# replace(s1, s2, s3) that returns a string equal to
# s1.replace(s2, s3), but again without calling s.replace().


def fun_replace(s1, s2, s3):
	# if s2 in s1:
	# 	pos = s1.index(s2)
	# 	print(pos)
	# 	return s1[0:pos] + s3 + s1[pos + len(s2):]
	# return s1
	return s1.replace(s2,s3)