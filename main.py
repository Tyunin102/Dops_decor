def memory(max_size):
    cache = {}

    def wrapper(func):
        def inner(*args, **kwargs):
            args_str = ','.join(map(str, args))
            kwargs_str = ','.join('{}={}'.format(key, value) for key, value in kwargs.items())
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

    return int(a) + int(b)

print(add(1,2))
print(add(1,'2'))
print(add(2,'1'))

print(add(a=4,b=3))
print(add(a='4', b=3))
print(add(a='4',b='3'))
