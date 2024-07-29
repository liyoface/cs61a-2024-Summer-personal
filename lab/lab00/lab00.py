def twenty_twenty():
    """Come up with the most creative expression that evaluates to 2020,
    using only numbers and the +, *, and - operators.

    >>> twenty_twenty()
    2020
    """
    x=1000
    x *= 2
    x += 20
    return x

if __name__ == '__main__':
    print(twenty_twenty())

