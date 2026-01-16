# Goal: Write @cache decorator that stores results of expensive function calls in a dictionary.

# Deep dive: If func(5) is called, check the dict. If key 5 exists, return it instantly (O(1)).
#            If not, run the function and save the result. This optimizes recursion(e.g. Fibonacci).

def cache(func):
    memo={}
    def wrap(n):
        if n in memo:
            return memo[n]
        memo[n] = func(n)
        return memo[n]
    return wrap

@cache
def fibo(n):
    if n<=1 :
        return n
    return fibo(n-1) + fibo(n-2)

print(fibo(12))

print(fibo.__name__)