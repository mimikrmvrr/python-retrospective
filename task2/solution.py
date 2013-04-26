def groupby(func, seq):
    result = {}
    for value in seq:
        result.setdefault(func(value), []).append(value)
    return result


def comp(function1, function2):
    return (lambda arg: function1(function2(arg)))


def iterate(func):
    function = lambda arg: arg
    while True:
        yield function
        function = comp(func, function)


def zip_with(func, *iterables):
    if len(iterables) < 1:
        return []
    else:
        return (func(*elements) for elements in zip(*iterables))


def cache(func, cache_size):
    if cache_size == 0:
        return func
    else:
        cache_results = {}
        cache_order = []
        front_index = 0

        def func_cached(*args):
            nonlocal cache_results, cache_order, front_index
            if not args in cache_results:
                result = func(*args)
                cache_order.append(args)
                cache_results[args] = result
                if (len(cache_order) - front_index) > cache_size:
                    del cache_results[cache_order[front_index]]
                    front_index += 1
            return cache_results[args]

    return func_cached
