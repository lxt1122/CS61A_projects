def printed(f):
    """
    >>> printed_pow = printed(pow)
    >>> printed_pow(2, 8)  # *args represents the arguments (2, 8)
    Result: 256
    256
    >>> printed_abs = printed(abs)
    >>> printed_abs(-10)  # *args represents one argument (-10)
    Result: 10
    10
    """
     
    def print_and_return(*args):
        result = f(*args)
        print('Result:', result)
        return result
    return print_and_return
