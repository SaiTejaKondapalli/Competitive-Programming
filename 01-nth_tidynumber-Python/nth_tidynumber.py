# Write the function nthTidyNumber that takes a non-negative int n and returns the nth Tidy Number.
# A tidy number is a number whose digits are in non-decreasing order.
# fun_nth_tidynumber(0) = 1
# fun_nth_tidynumber(1) = 2
# fun_nth_tidynumber(5) = 6
# fun_nth_tidynumber(15) = 17
# fun_nth_tidynumber(35) = 46

def istidy(n):
    if int("".join(sorted(str(n)))) == n:
        return True
    return False

def fun_nth_tidynumber(n):
    count = 0
    i = 0
    while True:
        if istidy(i):
            if count == n:
                return i
            count += 1
        i += 1