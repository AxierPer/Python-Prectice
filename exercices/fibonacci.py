from functools import lru_cache

@lru_cache(maxsize=16)
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci (n-2)


number = 0

while number <= 30:
    print(fibonacci(number))
    number = number + 1
