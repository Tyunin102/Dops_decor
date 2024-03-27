def memory(max_size):
    cache = {}

    def wrapper(func):
        def inner(*args, **kwargs):
            args_str = ','.join(map(str, sorted(args)))
            sorted_kwargs = sorted(kwargs.items())
            kwargs_str = ','.join('{}={}'.format(key, value) for key, value in sorted_kwargs)
            key = '{}|{}'.format(args_str, kwargs_str)
            print(f"{key} is a key")
            if key in cache:
                print(f"{key} in cache")
                return cache[key]
            else:
                result = func(*args, **kwargs)
                if len(cache) >= max_size:
                    print('cache is full')
                else:
                    cache[key]=result
                return result
        return inner
    return wrapper

@memory(max_size=int(input()))
def add(a, b):

    return a + b


print(add(1, 2))
print(add(2, 1))

print(add(a=1,b=2))
print(add(b=2,a=1))
print(add(3,4))
print(add(a=4,b=3))
