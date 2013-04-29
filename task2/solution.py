from collections import OrderedDict


def groupby(func, seq):
    result = {}
    for value in seq:
        result.setdefault(func(value), []).append(value)
    return result


def comp(function1, function2):
    return lambda arg: function1(function2(arg))


def iterate(func):
    function = lambda arg: arg
    while True:
        yield function
        function = comp(func, function)


def zip_with(func, *iterables):
    if len(iterables) < 1:
        return []
    return (func(*elements) for elements in zip(*iterables))


def cache(func, cache_size):
    if cache_size == 0:
        return func
    cached_results = OrderedDict()

    def func_cached(*args):
        if not args in cached_results:            
            cached_results[args] = func(*args)
            if len(cached_results) > cache_size:
                cached_results.popitem(last=False)
        return  cached_results[args]

    return func_cached
