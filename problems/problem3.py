"""
The prime factors of 13195 are 5, 7, 13 and 29.What is the largest prime factor of the number 600851475143 ?Note: This problem has been changed recently, please check that you are using the right number.

http://www.projecteuler.net/index.php?section=problems&id=3
"""
from math import sqrt

val1 = 600851475143
val2 = int(sqrt(val1))

prime_factors = []


def is_prime(n):
    """Checks if n is prime"""
    divisors = range(3, int(sqrt(n)), 2)
    for num in divisors:
        if (not n%num):
            return False 

    return True

def problem_3():
    print "Sit back. This is going to take a while."
    n = 3
    while n < val2:
        if is_prime(n) and (not val1%n): #if n is prime and val1 is evenly divisible by n
            prime_factors.append(n)
        n += 2

    print "The largest prime factor of %d is %d" % (val1, prime_factors[-1])
