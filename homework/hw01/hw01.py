from operator import add, sub
import math

def a_plus_abs_b(a, b):

    if b >= 0:
        h = a + b
    else:
        h = a + (-b)
    return h


def two_of_three(x, y, z):

    return ((x*x) + (y*y) + (z*z)) - max(x,y,z)*max(x,y,z)

def if_function(condition, true_, false_):

    if (condition):
        return true_
    else: return false_

def with_if_statment():
    if cond():
        return true_func()
    else: return false_func()

def with_if_function():
    """
    >>> result = with_if_function()
    42
    47
    >>> print(result)
    None
    """
    return if_function(cond(), true_func(), false_func())

def cond():
    "*** YOUR CODE HERE ***"
    return True
def true_func():
    "*** YOUR CODE HERE ***"
    print(42)
def false_func():
    "*** YOUR CODE HERE ***"
    print(47)

def HailStone(num):
    step = 1
    while(num != 1):
        print(num)
        step += 1
        if (num % 2== 0): num //= 2
        else: num = num*3 + 1

    return step

a = HailStone(27)
print(a)