def digit(n, k):
    """Return the digit that is k from the right of n for positive integers n and k.

    >>> digit(3579, 2)
    5
    >>> digit(3579, 0)
    9
    >>> digit(3579, 10)
    0
    """
    d = [];
    d.append(n % 10);
    m = 10;
    n_l = len(str(n));
    while n_l > 0:
        n_l -= 1;
        d.append((int)(n / m) % 10);

        m *= 10;
        
    if (k > len(str(n))):
        return 0;
    else:
        return d[k];


def middle(a, b, c):
    """Return the number among a, b, and c that is not the smallest or largest.
    Assume a, b, and c are all different numbers.

    >>> middle(3, 5, 4)
    4
    >>> middle(30, 5, 4)
    5
    >>> middle(3, 5, 40)
    5
    >>> middle(3, 5, 40)
    5
    >>> middle(30, 5, 40)
    30
    """
    sum_ = a + b + c;

    return sum_ - max(a,b,c) - min(a,b,c);


def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    fac = 1;
    while k > 0:
        k -= 1;
        
        fac *= n;
        
        n -= 1;

    return fac;


def divisible_by_k(n, k):
    """
    >>> a = divisible_by_k(10, 2)  # 2, 4, 6, 8, and 10 are divisible by 2
    2
    4
    6
    8
    10
    >>> a
    5
    >>> b = divisible_by_k(3, 1)  # 1, 2, and 3 are divisible by 1
    1
    2
    3
    >>> b
    3
    >>> c = divisible_by_k(6, 7)  # There are no integers up to 6 divisible by 7
    >>> c
    "***YOUR CODE HERE ***"
    """
    num = 0;
    if n % k != 0 and k > n:
        return 0;
    else:
        for i in range(k, n+k, k):
            num += 1;
            print(i);
        return num;
    


def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    sum_ = 0;
    index = len(str(y));
    x = 1;
    while index > 0:
        sum_ += (int)(y / x % 10);
        index -= 1;
        x *= 10;
    return sum_;
    


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    index = len(str(n));
    x = 1;
    flag = 0;
    while index > 0:
        
        if (int)(n / x % 10) == 8:
            flag += 1;
        x *= 10;
        index -= 1;

    if flag == 2:
        return True;
    else:
        return False;

