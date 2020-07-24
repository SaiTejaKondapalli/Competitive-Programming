# Write the function nthLeftTruncatablePrime(n).
# A Left-truncatable prime is a prime which in a given base (say 10) does not contain 0
# and which remains prime when the leading (left) digit is successively removed.
# For example, 317 is left-truncatable prime since 317, 17 and 7 are all prime.
# There are total 4260 left-truncatable primes.
# So nthLeftTruncatablePrime(0) retunearestKaprekarNumber(n)rns 2, and
# nthLeftTruncatablePrime(10) returns 53.


import math
def isprime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True
    # count = 0
    # for i in range(1,n+1):
    #     if n % i == 0:
    #         count += 1
    # return count == 2
def truncatableprime(n):
    if "0" in str(n):
        return False
    if len(str(n)) == 1:
        return isprime(n)
    while len(str(n)) > 1:
        i = int(str(n)[1:])
        if not isprime(i):
            return False
    return True
    # for i in range(1, len(s)):
    #     if not isprime(int(s[i:])):
    #         return False
    # return True

def fun_nth_lefttruncatableprime(n):
    i = 1
    count = 0
    while True:
        if truncatableprime(i) and isprime(i):
            if count == n:
                return i
            count += 1
        i += 1


