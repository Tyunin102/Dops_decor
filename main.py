def memory(max_size):
    cache = {}

    def wrapper(func):
        def inner(*args, **kwargs):
            # Формируем отсортированный кортеж из аргументов для создания ключа
            key = tuple(sorted(args + tuple(kwargs.values())))

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

# Пример использования
print(add(1, 2)) 
print(add(a=1,b=2))
print(add(3,4))
print(add(a=4,b=3))

