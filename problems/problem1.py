"""
If we list all of the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

http://www.projecteuler.net/index.php?section=problems&id=1
"""


def problem_1():
    print "The sum of all natural numbers below 1000 that are multiples of 3 and 5 is %d" % sum(filter(multiple_of_3_or_5, range(1, 1000)))


def multiple_of_3_or_5(n):
    """Returns true if n is divisible by 3 or 5"""
    return (not (n%3)) or (not (n%5))

