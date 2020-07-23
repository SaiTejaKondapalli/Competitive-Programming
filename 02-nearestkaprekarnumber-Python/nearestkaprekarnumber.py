# Note: please do not start this problem prior to completing previous problem.
# Bearing in mind the definition of Kaprekar Number from above problem, write the function
# nearestKaprekarNumber(n) that takes an int value n and returns the Kaprekar number
# closest to n, with ties going to smaller value. For example, nearestKaprekarNumber(49) returns 45,
# and nearestKaprekarNumber(51) returns 55. And since ties go to the smaller number,
# nearestKaprekarNumber(50) returns 45.
# Note: as you probably guessed, this also cannot be solved by counting up from 0,
# as that will not be efficient enough to get past the autograder.
# Hint: one way to solve this is to start at n and grow in each direction until you find a Kaprekar number.



import math

def fun_nearestkaprekarnumber(n):
    i = n
    d1 = 0
    d2 = 0
    while True:
        flag = 0
        square = i ** 2
        sq = str(square)
        for j in range(1, len(sq)):
            left = int("".join(sq[:j]))
            right = int("".join(sq[j:]))
            if right == 0:
                continue
            if left + right == i:
                flag = 1
                d1 = i
                break
        if flag == 1:
            break
        i += 1
    k = n
    while True:
        flag = 0
        square = k ** 2
        sq = str(square)
        for j in range(1, len(sq)):
            left = int("".join(sq[:j]))
            right = int("".join(sq[j:]))
            if right == 0:
                continue
            if left + right == k:
                flag = 1
                d2 = k
                break
        if flag == 1:
            break
        k -= 1
    if abs(d1 - n) == abs(d2 - n):
        return d2
    if abs(d1 - n) > abs(d2 - n):
        return d2
    else:
        return d1
