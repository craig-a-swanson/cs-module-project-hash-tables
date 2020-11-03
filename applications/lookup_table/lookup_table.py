import random
import math


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v


power_cache = {}
factorial_cache = {}

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """

    # start populating a cache for the power function
    if (x, y) not in power_cache:
        power_cache[(x, y)] = math.pow(x, y)
    # retrieve the value associated with the cache key
    v = power_cache[(x, y)]

    # start populating a cache for the factorial function
    if v not in factorial_cache:
        factorial_cache[v] = math.factorial(v)
    # retrieve the value associated with the cache key
    v = factorial_cache[v]
    
    v //= (x + y)
    v %= 982451653

    return v



# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
