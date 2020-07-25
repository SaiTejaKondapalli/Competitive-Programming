# Write the function nthUglyNumber that takes a non-negative int n and returns the nth Ugly Number.
# Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8,
# 9, 10, 12, 15 shows the few ugly numbers. By convention, nthUglyNumber(0) will give 1.

def div(a, b):
    while a % b == 0:
        a /= b
    return a

def isugly(num):
    num = div(num, 2)
    num = div(num, 3)
    num = div(num, 5)
    if num == 1:
        return True
    return False
def fun_nth_uglynumber(n):
    i = 1
    count = 0
    while True:
        if isugly(i):
            if count == n:
                return i
            count += 1
        i += 1
