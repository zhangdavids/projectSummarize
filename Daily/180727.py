def memoize(f):
    """
    计划性的缓存
    """
    call_cache = dict()

    def memoized(argument):
        try:
            return call_cache[argument]
        except KeyError:
            return call_cache.setdefault(argument, f(argument))

    return memoized


@memoize
def fibonacci(n):
    if n < 3:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':

    print(fibonacci(10))
    print(fibonacci(20))
