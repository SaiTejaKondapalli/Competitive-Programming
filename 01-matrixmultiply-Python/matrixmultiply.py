# Write the function matrixMultiply(m1, m2) that takes two 2d lists
# (that we will consider to be matrices) and returns a new 2d list that
# is the result of multiplying the two matrices. Return None if the
# two matrices cannot be multiplied for any reason.

import numpy as np
def fun_matrixmultiply(m1, m2):
    res = np.zeros([m1.length,m2[0].length])
    if m1[0].length != m2.length:
        return None
    else:
        for i in range(m1.length):
            for j in range(m2[0].length):
                for k in range(m2.length):
                    res[i][j] += m1[i][k] * m2[k][j]
        return res




