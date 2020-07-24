# Happy Primes [20 pts]
# Background: read the first paragraph from the Wikipedia page on happy numbers. After
# some thought, we see that no matter what number we start with, when we keep replacing
# the number by the sum of the squares of its digits, we'll always either arrive at 4 (
# unhappy) or at 1 (happy). With that in mind, we want to write the function nthHappyNumber
# (n). However, to write that function, we'll first need to write isHappyNumber(n) (
# right?). And to write that function, we'll first need to write sumOfSquaresOfDigits(n).
# And that's top-down design! Here we go....
# Note: the autograder will grade each of the following functions, so they are required.
# However, they also are here specifically because they are just the right helper
# functions to make nthHappyNumber(n) easier to write!

def sumofdigits(n):
    summ = 0
    while n > 0:
        dig = n % 10
        summ += dig * dig
        n = n // 10
    return summ

def ishappy(n):
    s = set()
    s.add(n)
    while True:
        if n == 1:
            return True
        n = sumofdigits(n)
        if n in s:
            return False
        s.add(n)
    return False

def isprime(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count == 2

def ishappyprimenumber(n):
    # Your code goes here
    if ishappy(n) and isprime(n):
        return True
    return False