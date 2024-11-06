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

result = with_if_statment()
print(result)