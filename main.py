def memory(max_size):
    cache = {}
    cache_order = []

    def wrapper(func):
        def inner(*args):
            if args in cache:
                print(f"{args} in cache")
                cache_order.remove(args)
                cache_order.append(args)
                return cache[args]
            else:
                print(f"{args} not in cache")
                result = func(*args)
                cache[args] = result
                cache_order.append(args)

                if len(cache_order) > max_size:
                    print('cache is full')
                    oldest_args = cache_order.pop(0)
                    del cache[oldest_args]
                return result
        return inner
    return wrapper


@memory(max_size=int(input()))
def add(a,b):
    return a+b

if __name__ == '__main__':
    print(add(2,3))
    print(add(1,3))
    print(add(3,3))

